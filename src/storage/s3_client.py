import boto3
from botocore.client import BaseClient

from src.config.settings import settings


def get_s3_client() -> BaseClient:
    """
    Create an S3-compatible client.

    Works with both MinIO and AWS S3.
    """

    if not settings.S3_ENDPOINT_URL:
        raise ValueError(
            "S3_ENDPOINT_URL is not configured."
        )

    return boto3.client(
        "s3",
        endpoint_url=settings.S3_ENDPOINT_URL,
        aws_access_key_id=settings.S3_ACCESS_KEY,
        aws_secret_access_key=settings.S3_SECRET_KEY,
        region_name=settings.S3_REGION,
    )