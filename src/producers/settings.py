class BaseURLs:
    PUBLIC_TRANSIT_STATUS_URL: str
    LANDOOP_KAFKA_CONNECT: str
    LANDOOP_KAFKA_TOPICS: str
    LANDOOP_KAFKA_SCHEMA_REGISTRY: str
    KAFKA_BROKER_URL: str
    KAFKA_REST_PROXY_URL: str
    KAFKA_SCHEMA_REGISTRY_URL: str
    KAFKA_CONNECT_URL: str
    KSQL_URL: str
    POSTGRESSQL_URL: str
    POSTGRES_USERNAME: str = "cta_admin"
    POSTGRES_PASSWORD: str = "chicago"
    DIALECT: str = "PostgreSqlDatabaseDialect"


class DockerURLs(BaseURLs):
    PUBLIC_TRANSIT_STATUS_URL: str = "http://localhost:8888"
    LANDOOP_KAFKA_CONNECT: str = "http://connect-ui:8084"
    LANDOOP_KAFKA_TOPICS: str = "http://topics-ui:8085"
    LANDOOP_KAFKA_SCHEMA_REGISTRY: str = "http://schema-registry-ui:8086"
    KAFKA_BROKER_URL: str = "PLAINTEXT://kafka0:9092,PLAINTEXT://kafka1:9093,PLAINTEXT://kafka2:9094"
    KAFKA_REST_PROXY_URL: str = "http://rest-proxy:8082/"
    KAFKA_SCHEMA_REGISTRY_URL: str = "http://schema-registry:8081/"
    KAFKA_CONNECT_URL: str = "http://kafka-connect:8083"
    KSQL_URL: str = "http://ksql:8088"
    POSTGRESSQL_URL = "jdbc:postgresql://postgres:5432/cta"


class LocalURLs(BaseURLs):
    PUBLIC_TRANSIT_STATUS_URL: str = "http://localhost:8888"
    LANDOOP_KAFKA_CONNECT: str = "http://localhost:8084"
    LANDOOP_KAFKA_TOPICS: str = "http://localhost:8085"
    LANDOOP_KAFKA_SCHEMA_REGISTRY: str = "http://localhost:8086"
    KAFKA_BROKER_URL: str = "PLAINTEXT://localhost:9092"
    KAFKA_REST_PROXY_URL: str = "http://localhost:8082"
    KAFKA_SCHEMA_REGISTRY_URL: str = "http://localhost:8081"
    KAFKA_CONNECT_URL: str = "http://localhost:8083"
    KSQL_URL: str = "http://localhost:8088"
    # "jdbc:postgresql://localhost:5432/cta"
    POSTGRESSQL_URL: str = "jdbc:postgresql://localhost:5432/cta"
    POSTGRES_USERNAME: str = "cta_admin"
    POSTGRES_PASSWORD: str = "chicago"


class Settings:
    URLs: BaseURLs = LocalURLs
