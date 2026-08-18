import pandas as pd

from src.transformation.market_transform import (
    transform_market_data,
    clean_market_data,
)


def test_transform_market_data():
    raw_data = {
        "bitcoin": {
            "usd": 64273,
            "usd_market_cap": 1290000000000,
            "usd_24h_vol": 20000000000,
            "usd_24h_change": 1.14,
            "last_updated_at": 1787062040,
        },
        "ethereum": {
            "usd": 1898.7,
            "usd_market_cap": 229000000000,
            "usd_24h_vol": 5800000000,
            "usd_24h_change": -0.01,
            "last_updated_at": 1787062030,
        },
    }

    df = transform_market_data(raw_data)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2

    assert list(df["coin_id"]) == [
        "bitcoin",
        "ethereum",
    ]

    assert df.loc[0, "price_usd"] == 64273
    assert df.loc[1, "price_usd"] == 1898.7

    assert isinstance(
    df["last_updated_at"].dtype,
    pd.DatetimeTZDtype,
    )


def test_clean_market_data():
    df = pd.DataFrame(
        {
            "coin_id": [" Bitcoin ", "ethereum", "bitcoin"],
            "price_usd": [64000, 1900, 65000],
            "market_cap_usd": [
                1.2e12,
                2.3e11,
                1.25e12,
            ],
            "volume_24h_usd": [
                2.0e10,
                6.0e9,
                2.1e10,
            ],
            "change_24h_pct": [
                1.5,
                -0.5,
                0.0,
            ],
            "last_updated_at": pd.to_datetime(
                [
                    "2026-08-18 14:00:00",
                    "2026-08-18 14:00:00",
                    "2026-08-18 14:05:00",
                ],
                utc=True,
            ),
        }
    )

    cleaned = clean_market_data(df)

    assert len(cleaned) == 2

    assert "bitcoin" in cleaned["coin_id"].values
    assert "ethereum" in cleaned["coin_id"].values

    assert "market_cap_usd_billions" in cleaned.columns
    assert "volume_24h_usd_billions" in cleaned.columns
    assert "price_change_direction" in cleaned.columns

    bitcoin = cleaned[
        cleaned["coin_id"] == "bitcoin"
    ].iloc[0]

    assert bitcoin["price_change_direction"] == "unchanged"
