from pathlib import Path

from src.storage.s3_raw_storage import upload_raw_file


def main() -> None:
    raw_files = sorted(
        Path("data/raw").glob(
            "market_data_*.json"
        )
    )

    if not raw_files:
        raise FileNotFoundError(
            "No raw market data files found."
        )

    for raw_file in raw_files:
        object_key = upload_raw_file(raw_file)

        print(
            f"Uploaded: {raw_file.name}"
        )
        print(
            f"Object key: {object_key}"
        )


if __name__ == "__main__":
    main()