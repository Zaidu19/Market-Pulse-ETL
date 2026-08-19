from pathlib import Path

import pandas as pd

from src.loading.mongodb_client import (
    get_mongodb_client,
)
from src.loading.mongodb_loader import (
    get_market_collection,
    load_market_data,
)


def main() -> None:
    processed_files = sorted(
        Path("data/processed").glob(
            "market_data_*.csv"
        )
    )

    if not processed_files:
        raise FileNotFoundError(
            "No processed market data files found."
        )

    latest_file = processed_files[-1]

    df = pd.read_csv(latest_file)

    df["last_updated_at"] = pd.to_datetime(
        df["last_updated_at"],
        utc=True,
    )

    client = get_mongodb_client()

    try:
        collection = get_market_collection(client)

        processed_count = load_market_data(
            df,
            collection,
        )

        print(
            f"Successfully processed "
            f"{processed_count} market records."
        )

    finally:
        client.close()


if __name__ == "__main__":
    main()