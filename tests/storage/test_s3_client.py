import pytest

from src.config.settings import settings
from src.storage.s3_client import get_s3_client


def test_s3_endpoint_required(monkeypatch):
    monkeypatch.setattr(
        settings,
        "S3_ENDPOINT_URL",
        "",
    )

    with pytest.raises(
        ValueError,
        match="S3_ENDPOINT_URL is not configured",
    ):
        get_s3_client()