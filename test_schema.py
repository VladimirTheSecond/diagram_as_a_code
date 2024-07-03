from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.database import Oracle
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.analytics import Hive
from diagrams.onprem.queue import Kafka
from diagrams.custom import Custom

with Diagram("\n Схема потоков лучшей компании в мире", show=False):
    ingress = Hive("Какой-то Hive \n 10.54.34.777:35")
    mts = Custom("Пример кастомного \n поля", "mts-logo.png")

    metrics = Prometheus("metric")
    metrics << Edge(minlen="4") << Grafana("monitoring портал monitoring.best_company.ru")

    with Cluster("Cluster имени древнего бога"):
        grpcsvc = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    with Cluster("Sessions HA \n 34.23.21.322:333"):
        primary = Redis("session")
        primary - Redis("replica") << metrics
        grpcsvc >> primary

    with Cluster("PostgreSQL "):
        primary = PostgreSQL("он вам не Greenplum \n 23.23.34.45:34")
        primary - PostgreSQL("И он тоже не GP \n 34.89.876.555:3900") << metrics
        grpcsvc >> primary

    aggregator = Oracle("Storage \n 12.222.34.665:34")
    aggregator >> Kafka("stream") >> Spark("analytics")

    ingress >> Edge(color="black", style="bold", minlen="4") >> grpcsvc >> aggregator >> mts
