from datetime import datetime,timezone

import pandas as pd
from pymongo import ASCENDING,UpdateOne
from pymongo.collection import Collection

from src.config.settings import settings
from src.loading.mongodb_client import get_mongodb_client


def get_market_collection(
    client,
) -> Collection:
    """
    Return the market_data collection and ensure indexes exist.
    """

    database = client[settings.MONGODB_DATABASE]

    collection = database[
        settings.MONGODB_COLLECTION
    ]

    collection.create_index(
        [
            ("coin_id", ASCENDING),
            ("last_updated_at", ASCENDING),
        ],
        unique=True,
        name="unique_coin_snapshot",
    )

    return collection

def load_market_data(
    df:pd.DataFrame,
    collection:Collection,
) -> int:
    """
    Load Market data into MongoDB using bulk upserts.
    
    Returns:
        Number of records successfully processed.
    """

    if df.empty:
        return 0

    ingested_at =datetime.now(timezone.utc)

    operations =[]

    for record in df.to_dict(orient="records"):
        record["ingested_at"] = ingested_at

        operations.append(
            UpdateOne(
                {
                    "coin_id":record["coin_id"],
                    "last_updated_at":record["last_updated_at"],
                },
                {
                    "$set": record,
                },
                upsert=True
            )
        )

    result = collection.bulk_write(operations)

    return (
        result.upserted_count
        + result.modified_count
    )