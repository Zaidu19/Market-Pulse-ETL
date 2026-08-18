from src.config.settings import settings


def main() -> None:
    print("Market Pulse ETL")
    print(f"Environment: {settings.APP_ENV}")


if __name__ == "__main__":
    main()

