import json
from datetime import datetime, timezone
from pathlib import Path


RAW_DATA_DIR = Path("data/raw")


def save_raw_data(data: dict) -> Path:
    """
    Save raw API response as a timestamped JSON file.
    """

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = RAW_DATA_DIR / f"market_data_{timestamp}.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return file_path