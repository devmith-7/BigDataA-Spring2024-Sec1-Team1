
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import Redshift
from diagrams.aws.storage import S3
from diagrams.onprem.database import Cassandra
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import User
from diagrams.onprem.network import Internet
from diagrams.generic.blank import Blank

with Diagram("Lambda Architecture - Public Safety and Crime Reporting", show=False, direction="LR"):
    with Cluster("Batch Layer"):
        csv_data = S3("Boston Crime Data\n(CSV Files)")
        hadoop = EC2("Hadoop for Batch Processing\n&\n Incremental Processing")
        batch_storage = Redshift("Batch Storage\n+ Data\n Synchronization")
        csv_data >> hadoop >> batch_storage

    with Cluster("Speed Layer"):
        kafka_stream = Kafka("Kafka Stream\n+ Data Entry")
        spark_streaming = EC2("Spark for Stream Processing")
        real_time_view = Redis("Real-time View")
        kafka_stream >> spark_streaming >> real_time_view

    with Cluster("Serving Layer"):
        cassandra = Cassandra("Cassandra Database\n+ Data Merging")
        batch_storage >> cassandra
        real_time_view >> cassandra
        api = EC2("API Server")
        cassandra >> api

    with Cluster("Data Sources"):
        rapid_api_data = EC2("Rapid API\n(Crime Data)")
        spotcrime_alerts = Internet("Spotcrime Alerts\n(Web Scraping)")
        user_input_data = User("User-Generated Data")
        cron_job = EC2("Monthly Cron Job\nfor CSV Scraping")
        cron_job1 = EC2("Scraping Spotcrime\nperminute")
        boston_pd_csv_scrape = EC2("Boston PD\nCSV Data Scraping")
        rapid_api_data >> kafka_stream
        spotcrime_alerts >> cron_job1 >> kafka_stream
        user_input_data >> kafka_stream
        boston_pd_csv_scrape >> cron_job >> csv_data

    users = EC2("Users")
    users >> user_input_data
