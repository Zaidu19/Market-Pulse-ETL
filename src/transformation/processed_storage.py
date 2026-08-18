from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


PROCESSED_DATA_DIR = Path("data/processed")


def save_processed_data(df: pd.DataFrame) -> Path:
    """
    Save transformed market data as a timestamped CSV file.
    """

    PROCESSED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = (
        PROCESSED_DATA_DIR
        / f"market_data_{timestamp}.csv"
    )

    df.to_csv(
        file_path,
        index=False,
    )

    return file_path