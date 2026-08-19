from src.config.settings import settings
from src.storage.s3_client import get_s3_client


def main() -> None:
    client = get_s3_client()

    response = client.list_buckets()

    print("MinIO connection successful.")
    print(
        f"Buckets found: {len(response['Buckets'])}"
    )


if __name__ == "__main__":
    main()