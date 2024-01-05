"""
API:

Простой пример работы с API
"""

import requests

resource = requests.get("http://api.binance.com/api/v3/ticker/price")

for ticker in resource.json():
    if ticker["symbol"] == "BTCUSDT":
        print(ticker["price"])
