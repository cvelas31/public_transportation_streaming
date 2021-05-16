"""Configures a Kafka Connector for Postgres Station data"""
import json
import logging

import requests
from settings import Settings

logger = logging.getLogger(__name__)


KAFKA_CONNECT_URL = f"{Settings.URLs.KAFKA_CONNECT_URL}/connectors"
CONNECTOR_NAME = "stations"


def configure_connector():
    """Starts and configures the Kafka Connect connector"""
    logging.debug("Creating or updating kafka connect connector...")

    resp = requests.get(f"{KAFKA_CONNECT_URL}/{CONNECTOR_NAME}")
    if resp.status_code == 200:
        logging.debug("Connector already created skipping recreation")
        return

    config = {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",  # TODO
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable": "false",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "topic.prefix": "conn_prefix_",
        "connection.url": "jdbc:postgresql://localhost:5432/cta",
        "connection.user": "cta_admin",
        "connection.password": "chicago",
        "batch.max.rows": "500",
        "table.whitelist": "stations",
        "poll.interval.ms": "5000",  # Poll every 5 seconds
        "mode": "incrementing",
        "incrementing.column.name": "stop_id"
    }
    # TODO: Complete the Kafka Connect Config below.
    # Directions: Use the JDBC Source Connector to connect to Postgres. Load the `stations` table
    # using incrementing mode, with `stop_id` as the incrementing column name.
    # Make sure to think about what an appropriate topic prefix would be, and how frequently Kafka
    # Connect should run this connector (hint: not very often!)

    data = json.dumps({
        "name": CONNECTOR_NAME,
        "config": config
    })
    resp = requests.post(
        KAFKA_CONNECT_URL,
        headers={"Content-Type": "application/json"},
        data=data,
    )

    # Ensure a healthy response was given
    resp.raise_for_status()
    logging.info("Connector created successfully")


if __name__ == "__main__":
    configure_connector()
