# Case Study 1
Case Study for DAMG7245

## Part 1: Real-Time Public Safety and Crime Reporting Application

## Overview
This application provides real-time public safety and crime reporting capabilities. It uses modern data processing and analytics technologies to gather, process, and visualize crime data in real time, helping to enhance public safety awareness and response.

## Architecture
The application is built on a sophisticated architecture that includes real-time data processing, machine learning, and interactive analytics. Key components include:

- **Web Scraping Services**: Gathering data from `spotcrime.com` and `Rapid API`.
- **Kafka for Streaming**: Managing real-time data streams.
- **AWS S3 Data Lake**: Storing streamed data.
- **ELT Processes (Spark)**: Transforming data for analysis.
- **SQL Databases (PostgreSQL)**: Storing processed data.
- **Machine Learning Service (TensorFlow)**: Analyzing data for insights.
- **Analytics Engine (Spark)**: Driving data visualization and reporting.
- **AWS Analytics (QuickSight)**: Providing interactive data visualizations.
- **Monitoring (Prometheus/Grafana)**: Ensuring system health and performance.

## Key Features
- **Real-Time Crime Reporting**: Users can report crimes as they occur.
- **Data Analytics and Visualization**: Interactive dashboards provide insights into crime patterns and notification of crimes in the end user's neighborhood.
- **User Participation**: The community can contribute data via the application.

## Technology Stack
- Backend: FastAPI, Python
- Frontend: React
- Database: PostgreSQL
- Data Processing: Apache Spark, TensorFlow
- Data Streaming: Apache Kafka
- Monitoring: Prometheus, Grafana
- Analytics: AWS QuickSight


## Part 2: Public Safety and Crime Reporting Application

## Overview
The Public Safety and Crime Reporting application leverages a robust Lambda Architecture to provide real-time crime reporting and analytics. It integrates live data streams with historical crime data to offer comprehensive insights into public safety trends.

## Features
- **Real-Time Crime Alerts**: Stream live crime data and alerts.
- **Historical Crime Analysis**: Comprehensive analytics on historical crime data.
- **User Interaction**: Allows users to input and receive crime data.

## Architecture
The application uses Lambda Architecture, comprising:
- **Batch Layer**: Processes historical crime data for long-term analysis.
- **Speed Layer**: Handles real-time data for immediate insights.
- **Serving Layer**: Merges outputs from Batch and Speed layers for querying.

## Technologies Used
- **AWS S3**: Storage for historical data.
- **Apache Hadoop/Spark**: For data processing.
- **Apache Kafka**: Manages real-time data streams.
- **Redis**: In-memory database for real-time view.
- **AWS Redshift**: Data warehousing.
- **Cassandra**: Database for Serving Layer.
- **Python**: For backend development.
