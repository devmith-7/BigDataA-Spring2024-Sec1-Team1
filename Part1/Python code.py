


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.onprem.analytics import Spark
from diagrams.onprem.client import User
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.compute import Server  # Generic server as a placeholder
from diagrams.onprem.network import Internet
from diagrams.onprem.queue import Kafka
from diagrams.programming.framework import FastAPI



with Diagram("Real-Time Public Safety and Crime Reporting Application Architecture", show=False):
    internet = Internet("Web Scraping spotcrime.com")
    internet1 = Internet("Rapid Api")
    users = User("Users")
    users1 = User("User input Data")

    web_app = FastAPI("Web Application (React)")
    load_balancer = EC2("Load Balancer")
    web_server = EC2("Web Server (FastAPI)")
    auth_server = EC2("Auth Server (OAuth)")
    quicksight = EC2("AWS Analytics (QuickSight)")


    
    scraping_service_3 = EC2("Csv files")

    kafka = Kafka("Kafka for Streaming")
    s3_bucket = S3("S3 Bucket for Data Lake")

    sql_db = PostgreSQL("SQL DB (PostgreSQL)")
    sql_db1 = PostgreSQL("SQL DB (PostgreSQL)")
    elt_process1 = Spark("ELT Process (Spark)")


    elt_process = Spark("ELT Process (Spark)")
    ml_service = Server("ML Service (TensorFlow)")

    analytics_engine = Spark("Analytics Engine")
    monitoring = EC2("Monitoring (Prometheus/Grafana)")

    users >> web_app >> load_balancer >> web_server >> auth_server
    web_server >> [internet1, internet] >> kafka
    users1 >> kafka
    kafka >> s3_bucket >> elt_process >> sql_db
    scraping_service_3 >> elt_process1 >> sql_db1 >> ml_service
    
    sql_db >> ml_service
    ml_service >> analytics_engine
    analytics_engine >> monitoring
    sql_db >> quicksight
    sql_db1 >> quicksight
    web_app >> quicksight
    ml_service >> quicksight

