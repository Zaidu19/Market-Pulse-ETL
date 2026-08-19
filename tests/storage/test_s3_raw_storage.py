from pathlib import Path
from unittest.mock import MagicMock

import pytest

from src.config.settings import settings
from src.storage.s3_raw_storage import upload_raw_file


def test_upload_raw_file(tmp_path, monkeypatch):
    raw_file = tmp_path / "market_data_20260818_141533.json"
    raw_file.write_text(
        '{"bitcoin": {"usd": 64000}}',
        encoding="utf-8",
    )

    mock_client = MagicMock()

    monkeypatch.setattr(
        "src.storage.s3_raw_storage.get_s3_client",
        lambda: mock_client,
    )

    object_key = upload_raw_file(raw_file)

    expected_key = (
        "raw/market_data/"
        "2026/08/18/"
        "market_data_20260818_141533.json"
    )

    assert object_key == expected_key

    mock_client.upload_file.assert_called_once_with(
        str(raw_file),
        settings.S3_BUCKET_NAME,
        expected_key,
    )


def test_upload_raw_file_not_found():
    with pytest.raises(FileNotFoundError):
        upload_raw_file(
            Path("data/raw/does_not_exist.json")
        )