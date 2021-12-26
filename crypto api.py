import requests
import pandas as pd

"""
It will get response from crypto api using requests library
"""
response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h")
jsonfile = response.json()
"""
converting response data to DataFrame
"""
df = pd.json_normalize(jsonfile)
"""
converting DataFrame to csv
"""
df.to_csv("crypto.csv", index=False)
