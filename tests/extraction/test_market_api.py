import pytest
import requests
from unittest.mock import patch

from src.extraction.market_api import fetch_market_data




@patch("src.extraction.market_api.requests.get")
def test_fetch_market_data_timeout(mock_get):
    mock_get.side_effect = requests.Timeout

    with pytest.raises(requests.RequestException):
        fetch_market_data(["bitcoin"]) 

def test_fetch_market_data_empty_coin_list():
    with pytest.raises(ValueError, match="coin_ids cannot be empty"):
        fetch_market_data([])           