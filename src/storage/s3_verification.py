from src.config.settings import settings
from src.storage.s3_client import get_s3_client


def list_raw_objects() -> list[str]:
    """
    Return all raw market-data object keys from the bucket.
    """

    client = get_s3_client()

    response = client.list_objects_v2(
        Bucket=settings.S3_BUCKET_NAME,
        Prefix="raw/market_data/",
    )

    objects = response.get("Contents", [])

    return [
        obj["Key"]
        for obj in objects
    ]