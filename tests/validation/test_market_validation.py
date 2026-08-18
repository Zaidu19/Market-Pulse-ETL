import pandas as pd
import pytest

from src.validation.market_validation import (
    validate_market_data,
)


def valid_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "coin_id": ["bitcoin", "ethereum"],
            "price_usd": [64000.0, 1900.0],
            "market_cap_usd": [1.2e12, 2.3e11],
            "volume_24h_usd": [2.0e10, 6.0e9],
            "change_24h_pct": [1.2, -0.5],
            "last_updated_at": pd.to_datetime(
                [
                    "2026-08-18 14:00:00",
                    "2026-08-18 14:00:00",
                ],
                utc=True,
            ),
        }
    )


def test_valid_market_data():
    df = valid_dataframe()

    validate_market_data(df)


def test_missing_price():
    df = valid_dataframe()
    df.loc[0, "price_usd"] = None

    with pytest.raises(
        ValueError,
        match="price_usd cannot contain null values",
    ):
        validate_market_data(df)


def test_invalid_price():
    df = valid_dataframe()
    df.loc[0, "price_usd"] = 0

    with pytest.raises(
        ValueError,
        match="price_usd must be greater than zero",
    ):
        validate_market_data(df)


def test_duplicate_coin():
    df = valid_dataframe()
    df.loc[1, "coin_id"] = "bitcoin"

    with pytest.raises(
        ValueError,
        match="Duplicate coin_id values found",
    ):
        validate_market_data(df)