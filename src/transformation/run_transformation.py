from pathlib import Path

from src.transformation.market_transform import (
    load_raw_data,
    transform_market_data,
    clean_market_data,
)

from src.transformation.processed_storage import(
    save_processed_data,
)
from src.validation.market_validation import validate_market_data


def main() -> None:
    raw_files = sorted(Path("data/raw").glob("market_data_*.json"))

    if not raw_files:
        raise FileNotFoundError(
            "No raw market data files found."
        )

    latest_file = raw_files[-1]

    data = load_raw_data(latest_file)

    df = transform_market_data(data)

    df = clean_market_data(df)

    validate_market_data(df)

    print("Market Data Validation Passed.")
    print()

    file_path = save_processed_data(df)
    print(f"Processed market data saved to: {file_path}")

   
    print(df)
    print()
    print(df.dtypes)


if __name__ == "__main__":
    main()