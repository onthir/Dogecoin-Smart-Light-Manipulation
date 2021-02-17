import json
import requests

# get the current doge value
def get_doge_price():
    endpoint = "https://www.cryptonator.com/api/ticker/doge-usd"
    # open
    response = requests.get(endpoint)
    data = response.json()

    return float(data["ticker"]["price"])

