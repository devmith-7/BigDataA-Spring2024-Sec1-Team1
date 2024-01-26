# Case Study 1
Case Study for DAMG7245


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
