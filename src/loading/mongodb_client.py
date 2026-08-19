from pymongo import MongoClient
from pymongo.database import Database

from src.config.settings import settings


def get_mongodb_client() -> MongoClient:
    """
    Create and return a MongoDB client.
    """

    if not settings.MONGODB_URI:
        raise ValueError("MONGODB_URI is not configured.")

    return MongoClient(
        settings.MONGODB_URI,
        serverSelectionTimeoutMS=5000,
    )


def get_database(client: MongoClient) -> Database:
    """
    Return the configured MongoDB database.
    """

    return client[settings.MONGODB_DATABASE]