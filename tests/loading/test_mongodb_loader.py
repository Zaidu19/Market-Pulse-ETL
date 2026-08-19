from unittest.mock import MagicMock

import pandas as pd

from src.loading.mongodb_loader import (
    get_market_collection,
    load_market_data,
)


def test_get_market_collection():
    client = MagicMock()

    database = client["market_pulse"]

    collection = database["market_data"]

    result = get_market_collection(client)

    assert result is collection

    collection.create_index.assert_called_once()


def test_load_market_data():
    df = pd.DataFrame(
        {
            "coin_id": ["bitcoin", "ethereum"],
            "price_usd": [64000.0, 1900.0],
            "market_cap_usd": [
                1.2e12,
                2.3e11,
            ],
            "volume_24h_usd": [
                2.0e10,
                6.0e9,
            ],
            "change_24h_pct": [
                1.5,
                -0.5,
            ],
            "last_updated_at": pd.to_datetime(
                [
                    "2026-08-18 14:00:00",
                    "2026-08-18 14:01:00",
                ],
                utc=True,
            ),
            "market_cap_usd_billions": [
                1200.0,
                230.0,
            ],
            "volume_24h_usd_billions": [
                20.0,
                6.0,
            ],
            "price_change_direction": [
                "up",
                "down",
            ],
        }
    )

    collection = MagicMock()

    result = MagicMock()
    result.upserted_count = 2
    result.modified_count = 0

    collection.bulk_write.return_value = result

    processed_count = load_market_data(
        df,
        collection,
    )

    assert processed_count == 2

    collection.bulk_write.assert_called_once()

    operations = (
        collection.bulk_write.call_args.args[0]
    )

    assert len(operations) == 2

def test_load_empty_market_data():
    df = pd.DataFrame()

    collection = MagicMock()

    result = load_market_data(
        df,
        collection,
    )

    assert result == 0

    collection.bulk_write.assert_not_called()


def test_load_market_data_uses_upsert():
    df = pd.DataFrame(
        {
            "coin_id": ["bitcoin"],
            "price_usd": [64000.0],
            "market_cap_usd": [1.2e12],
            "volume_24h_usd": [2.0e10],
            "change_24h_pct": [1.5],
            "last_updated_at": pd.to_datetime(
                ["2026-08-18 14:00:00"],
                utc=True,
            ),
            "market_cap_usd_billions": [1200.0],
            "volume_24h_usd_billions": [20.0],
            "price_change_direction": ["up"],
        }
    )

    collection = MagicMock()

    result = MagicMock()
    result.upserted_count = 1
    result.modified_count = 0

    collection.bulk_write.return_value = result

    load_market_data(df, collection)

    operation = (
        collection.bulk_write
        .call_args.args[0][0]
    )

    assert operation._upsert is True
