import requests
def get_data():
    """Fetch live exchange rate data."""
    url = "https://api.exchangerate.host/latest"
    params = {"base": "USD"}

    response = requests.get(url, params=params)

    if response.ok:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None