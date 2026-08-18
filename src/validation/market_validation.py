import pandas as pd


REQUIRED_COLUMNS = [
    "coin_id",
    "price_usd",
    "market_cap_usd",
    "volume_24h_usd",
    "change_24h_pct",
    "last_updated_at",
]


def validate_market_data(df: pd.DataFrame) -> None:
    """
    Validate the transformed market DataFrame.

    Raises:
        ValueError: If the DataFrame fails validation.
    """

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("Market DataFrame cannot be empty.")

    if df["coin_id"].isna().any():
        raise ValueError("coin_id cannot contain null values.")

    if df["price_usd"].isna().any():
        raise ValueError("price_usd cannot contain null values.")

    if (df["price_usd"] <= 0).any():
        raise ValueError("price_usd must be greater than zero.")

    if df["coin_id"].duplicated().any():
        raise ValueError("Duplicate coin_id values found.")

    if df["last_updated_at"].isna().any():
        raise ValueError(
            "last_updated_at cannot contain null values."
        )