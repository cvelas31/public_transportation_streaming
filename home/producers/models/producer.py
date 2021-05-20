"""Producer base-class providing common utilites and functionality"""
import logging
import time
from typing import Optional, Dict

from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer
from settings import Settings

logger = logging.getLogger(__name__)


SCHEMA_REGISTRY_URL = Settings.URLs.KAFKA_SCHEMA_REGISTRY_URL
#BROKER_URL = Settings.URLs.KAFKA_BROKER_URL
BROKER_URL = 'PLAINTEXT://localhost:9092,PLAINTEXT://localhost:9093,PLAINTEXT://localhost:9094'

print(f"BROKER_URL: {BROKER_URL}")
print(f"SCHEMA_REGISTRY_URL: {SCHEMA_REGISTRY_URL}")


class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema=None,
        num_partitions=1,
        num_replicas=1,
        config: Optional[Dict] = None
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas
        self.config = config

        #
        #
        # TODO: Configure the broker properties below. Make sure to reference the project README
        # and use the Host URL for Kafka and Schema Registry!
        self.broker_properties = {
            "schema.registry.url": SCHEMA_REGISTRY_URL,
            "bootstrap.servers": BROKER_URL,
            "linger.ms": 1000,
            "compression.type": "lz4"
        }

        # TODO: Validate it works with schema registry
        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # TODO: Configure the AvroProducer
        self.producer = AvroProducer(
            self.broker_properties,
            default_key_schema = self.key_schema,
            default_value_schema = self.value_schema
        )

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        #
        #
        # TODO: Write code that creates the topic for this producer if it does not already exist on
        # the Kafka Broker.
        #
        #
        client = AdminClient({"bootstrap.servers": self.broker_properties["bootstrap.servers"]})
        exists = self.topic_exists(client, self.topic_name)
        if not(exists):
            futures = client.create_topics([
                NewTopic(topic=self.topic_name,
                         num_partitions=self.num_partitions,
                         replication_factor=self.num_replicas,
                         config = {'cleanup.policy' : 'delete',
                                   'compression.type' : 'lz4', 
                                   'delete.retention.ms' : 2000, 
                                   'file.delete.delay.ms' : 10000}
                         )
            ])
            for _, future in futures.items():
                try:
                    future.result()
                    logging.debug(f"Topic {self.topic_name} created!")
                except Exception as e:
                    logging.error(
                        f"Topic {self.topic_name} could not be created")
                    logging.error(f"Error: {e}")

    @staticmethod
    def topic_exists(client, topic):
        """Checks if the given topic exists in Kafka"""
        topic_metadata = client.list_topics(timeout=5)
        exists = topic in set(t.topic for t in iter(topic_metadata.topics.values()))
        if exists:
            logging.warning(f"Topic {topic} already exists")
        return exists

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        #
        #
        # TODO: Write cleanup code for the Producer here
        #
        #
        self.producer.flush()
        logger.info("Flushing producer!")

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
