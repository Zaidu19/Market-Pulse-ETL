import json
from pathlib import Path

import pandas as pd


def load_raw_data(file_path: str | Path) -> dict:
    """
    Load raw market data from a JSON file.
    """

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def transform_market_data(data: dict) -> pd.DataFrame:
    """
    Transform raw market data into a structured DataFrame.
    """

    records = []

    for coin_id, values in data.items():
        records.append(
            {
                "coin_id": coin_id,
                "price_usd": values.get("usd"),
                "market_cap_usd": values.get("usd_market_cap"),
                "volume_24h_usd": values.get("usd_24h_vol"),
                "change_24h_pct": values.get("usd_24h_change"),
                "last_updated_at": values.get("last_updated_at"),
            }
        )

    df = pd.DataFrame(records)

    df["last_updated_at"] = pd.to_datetime(
        df["last_updated_at"],
        unit="s",
        utc=True,
    )

    return df


def clean_market_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and enrich transformed market data.
    """

    df = df.copy()

    # Clean coin identifiers
    df["coin_id"] = df["coin_id"].str.strip().str.lower()

    # Remove duplicate coins
    df = df.drop_duplicates(
        subset=["coin_id"],
        keep="last",
    )

    # Ensure numeric columns are numeric
    numeric_columns = [
        "price_usd",
        "market_cap_usd",
        "volume_24h_usd",
        "change_24h_pct",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    # Remove rows where critical numeric data is missing
    df = df.dropna(
        subset=[
            "coin_id",
            "price_usd",
            "market_cap_usd",
            "volume_24h_usd",
            "last_updated_at",
        ]
    )

    # Derived metrics
    df["market_cap_usd_billions"] = (
        df["market_cap_usd"] / 1_000_000_000
    )

    df["volume_24h_usd_billions"] = (
        df["volume_24h_usd"] / 1_000_000_000
    )

    df["price_change_direction"] = df[
        "change_24h_pct"
    ].apply(
        lambda value: (
            "up"
            if value > 0
            else "down"
            if value < 0
            else "unchanged"
        )
    )

    return df