import pandas as pd

import src.transformation.processed_storage as processed_storage


def test_save_processed_data(tmp_path):
    df = pd.DataFrame(
        {
            "coin_id": ["bitcoin"],
            "price_usd": [64000.0],
            "market_cap_usd": [1.2e12],
        }
    )

    processed_storage.PROCESSED_DATA_DIR = tmp_path

    file_path = processed_storage.save_processed_data(df)

    assert file_path.exists()
    assert file_path.suffix == ".csv"

    saved_df = pd.read_csv(file_path)

    assert len(saved_df) == 1
    assert saved_df.loc[0, "coin_id"] == "bitcoin"
    assert saved_df.loc[0, "price_usd"] == 64000.0