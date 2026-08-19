from unittest.mock import MagicMock

from src.storage.s3_verification import list_raw_objects


def test_list_raw_objects(monkeypatch):
    mock_client = MagicMock()

    mock_client.list_objects_v2.return_value = {
        "Contents": [
            {
                "Key": (
                    "raw/market_data/"
                    "2026/08/18/"
                    "market_data_20260818_141533.json"
                )
            },
            {
                "Key": (
                    "raw/market_data/"
                    "2026/08/18/"
                    "market_data_20260818_143338.json"
                )
            },
        ]
    }

    monkeypatch.setattr(
        "src.storage.s3_verification.get_s3_client",
        lambda: mock_client,
    )

    objects = list_raw_objects()

    assert len(objects) == 2

    assert objects[0].endswith(
        "market_data_20260818_141533.json"
    )

    mock_client.list_objects_v2.assert_called_once_with(
        Bucket="market-pulse-raw",
        Prefix="raw/market_data/",
    )