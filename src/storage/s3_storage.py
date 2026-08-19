from botocore.exceptions import ClientError

from src.config.settings import settings
from src.storage.s3_client import get_s3_client


def create_bucket() -> None:
    """
    Create the configured S3 bucket if it does not already exist.
    """

    client = get_s3_client()

    try:
        client.head_bucket(
            Bucket=settings.S3_BUCKET_NAME
        )
        print(
            f"Bucket already exists: "
            f"{settings.S3_BUCKET_NAME}"
        )
        return

    except ClientError:
        pass

    client.create_bucket(
        Bucket=settings.S3_BUCKET_NAME
    )

    print(
        f"Bucket created: "
        f"{settings.S3_BUCKET_NAME}"
    )