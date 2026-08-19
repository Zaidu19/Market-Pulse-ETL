import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "development")

    MONGODB_URI: str = os.getenv("MONGODB_URI", "")
    MONGODB_DATABASE: str = os.getenv(
        "MONGODB_DATABASE",
        "market_pulse",
    )
    MONGODB_COLLECTION: str = os.getenv(
    "MONGODB_COLLECTION",
    "market_data",
    )


    S3_ENDPOINT_URL: str = os.getenv(
    "S3_ENDPOINT_URL",
    ""
    )

    S3_BUCKET_NAME: str = os.getenv(
        "S3_BUCKET_NAME",
        "market-pulse-raw"
    )

    S3_ACCESS_KEY: str = os.getenv(
        "S3_ACCESS_KEY",
        ""
    )

    S3_SECRET_KEY: str = os.getenv(
        "S3_SECRET_KEY",
        ""
    )

    S3_REGION: str = os.getenv(
        "S3_REGION",
        "us-east-1"
    )

    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_REGION: str = os.getenv("AWS_REGION", "")
    
    MARKET_API_KEY: str = os.getenv("MARKET_API_KEY", "")
    MARKET_API_BASE_URL: str = os.getenv(
        "MARKET_API_BASE_URL",
        "",
    )


settings = Settings()