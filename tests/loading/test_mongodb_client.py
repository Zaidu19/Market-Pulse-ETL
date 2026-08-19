import pytest

from src.config.settings import settings
from src.loading.mongodb_client import get_mongodb_client


def test_mongodb_uri_required(monkeypatch):
    monkeypatch.setattr(
        settings,
        "MONGODB_URI",
        "",
    )

    with pytest.raises(
        ValueError,
        match="MONGODB_URI is not configured",
    ):
        get_mongodb_client()