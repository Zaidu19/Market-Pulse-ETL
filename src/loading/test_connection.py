from src.loading.mongodb_client import (
    get_database,
    get_mongodb_client,
)


def main() -> None:
    client = get_mongodb_client()

    try:
        client.admin.command("ping")

        database = get_database(client)

        print("MongoDB connection successful.")
        print(f"Database: {database.name}")

    finally:
        client.close()


if __name__ == "__main__":
    main()

