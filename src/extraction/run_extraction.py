from src.extraction.market_api import fetch_market_data
from src.extraction.raw_storage import save_raw_data
from src.utils.logger import get_logger
from src.storage.s3_raw_storage import upload_raw_file

logger = get_logger(__name__)


def main() -> None:
    coins = ["bitcoin", "ethereum"]

    logger.info("Starting market data extraction")

    data = fetch_market_data(coins)

    logger.info("Successfully extracted data for %d coins", len(data))

    file_path = save_raw_data(data)

    logger.info("Raw market data saved to %s", file_path)

    object_key = upload_raw_file(file_path)

    logger.info(
        "Raw market data uploaded to MinIO: %s",
        object_key,
    )


if __name__ == "__main__":
    main()