from datetime import datetime
from pathlib import Path

from src.config.settings import settings
from src.storage.s3_client import get_s3_client


def upload_raw_file(file_path: str | Path) -> str:
    """
    Upload a raw JSON file to S3-compatible storage.

    Returns:
        The S3 object key.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Raw file not found: {path}"
        )

    timestamp = datetime.strptime(
        path.stem.replace("market_data_", ""),
        "%Y%m%d_%H%M%S",
    )

    object_key = (
        f"raw/market_data/"
        f"{timestamp:%Y/%m/%d}/"
        f"{path.name}"
    )

    client = get_s3_client()

    client.upload_file(
        str(path),
        settings.S3_BUCKET_NAME,
        object_key,
    )

    return object_key