from unittest.mock import patch


@patch("src.extraction.run_extraction.upload_raw_file")
@patch("src.extraction.run_extraction.save_raw_data")
@patch("src.extraction.run_extraction.fetch_market_data")
def test_extraction_pipeline(
    mock_fetch,
    mock_save,
    mock_upload,
):
    mock_fetch.return_value = {
        "bitcoin": {
            "usd": 64000,
        },
        "ethereum": {
            "usd": 1900,
        },
    }

    mock_save.return_value = (
        "data/raw/market_data_test.json"
    )

    mock_upload.return_value = (
        "raw/market_data/2026/08/19/"
        "market_data_test.json"
    )

    from src.extraction.run_extraction import main

    main()

    mock_fetch.assert_called_once_with(
        ["bitcoin", "ethereum"]
    )

    mock_save.assert_called_once_with(
        mock_fetch.return_value
    )

    mock_upload.assert_called_once_with(
        mock_save.return_value
    )