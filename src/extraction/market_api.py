import requests


BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_market_data(
    coin_ids: list[str],
    vs_currency: str = "usd",
) -> dict:
    if not coin_ids:
        raise ValueError("coin_ids cannot be empty.")
    """
    Fetch current cryptocurrency market data from CoinGecko.


    Raises:
        requests.HTTPError: If the API returns an unsuccessful status.
        requests.RequetsException:If the request fails.
    """

    endpoint = f"{BASE_URL}/simple/price"

    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": vs_currency,
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true",
        "include_last_updated_at": "true",
    }
    try:
        response = requests.get(
            endpoint,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()
    except requests.Timeout as exc:
        raise requests.RequestException(
            "CoinGecko API request timed out."
        ) from exc

    except requests.ConnectionError as exc:
        raise requests.RequestException(
            "Unable to connect to CoinGecko API."
        ) from exc    