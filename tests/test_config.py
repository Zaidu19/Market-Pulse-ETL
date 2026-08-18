from src.config.settings import settings


def test_default_environment():
    assert settings.APP_ENV == "development"