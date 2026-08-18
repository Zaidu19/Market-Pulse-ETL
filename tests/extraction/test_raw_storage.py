from src.extraction.raw_storage import save_raw_data


def test_save_raw_data(tmp_path):
    data = {
        "bitcoin": {
            "usd": 100000
        }
    }

    raw_data_dir = tmp_path / "raw"

    import src.extraction.raw_storage as raw_storage

    raw_storage.RAW_DATA_DIR = raw_data_dir

    file_path = save_raw_data(data)

    assert file_path.exists()
    assert file_path.suffix == ".json"