# Sales Management ETL & Analytics Project

## Overview
This project implements an end-to-end data pipeline that extracts raw sales data from a CSV file, loads it into a SQLite database, performs analysis, and generates visual business reports.

The goal is to simulate how companies process raw business data into meaningful insights.


## Features
- ETL Pipeline (Extract → Transform → Load)
- Database storage using SQLite
- Monthly sales trend analysis
- Revenue by category analysis
- Automatic chart generation


## Tech Stack
Python  
Pandas  
Matplotlib  
SQLite  


## Project Workflow
1. Read raw sales dataset
2. Clean and transform data
3. Store into database
4. Perform analysis queries
5. Generate visual reports



## Run in 30 seconds

Install dependencies:
pip install -r requirements.txt

Load data into database:
python etl_pipeline.py

Generate reports:
python report.py


## Output
The project generates business insights such as sales trends and category revenue which help companies make decisions.
