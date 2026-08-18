# Market Pulse ETL

A production-style market data ETL platform built with Python, Pandas,
MongoDB, Apache Airflow, AWS S3, FastAPI, Docker, and GitHub Actions.

## Architecture

External Market API
        ↓
Extraction
        ↓
AWS S3 / Raw Data
        ↓
Transformation with Pandas
        ↓
Data Validation
        ↓
MongoDB
        ↓
FastAPI
        ↓
Consumers / Analytics

Apache Airflow orchestrates the ETL pipeline.

## Tech Stack

- Python
- Pandas
- MongoDB
- FastAPI
- Apache Airflow
- AWS S3
- Docker
- GitHub Actions
- Pytest

## Project Status

Phase 1 — Foundation 🚧