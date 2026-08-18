from src.extraction.market_api import fetch_market_data
from src.extraction.raw_storage import save_raw_data
from src.utils.logger import get_logger


logger = get_logger(__name__)


def main() -> None:
    coins = ["bitcoin", "ethereum"]

    logger.info("Starting market data extraction")

    data = fetch_market_data(coins)

    logger.info("Successfully extracted data for %d coins", len(data))

    file_path = save_raw_data(data)

    logger.info("Raw market data saved to %s", file_path)


if __name__ == "__main__":
    main()