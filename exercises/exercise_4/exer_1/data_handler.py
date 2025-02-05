import requests
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()
API_KEY = os.getenv("API_KEY")

db_user = os.getenv("POSTGRES_USER")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

def get_prices():
    URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {"slug": "bitcoin,ethereum", "convert": "USD"}
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}

    response = requests.get(url=URL, headers=headers, params=parameters)
    response.raise_for_status()
    data = response.json()["data"]
    # prices = data["data"]
    for coin_id, coin_data in data.items():
        print(f"Coin name = {coin_data["name"]}")
        for currency, data in coin_data["quote"].items():
            print(f"{data["price"]} USD")
            print(f"{data["percent_change_30d"]:.2f}% change last 30 days")
        print()


def get_listing():
    URL_listing = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {"limit": "10", "convert": "USD", "sort": "volume_7d"}
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}
    response = requests.get(url=URL_listing, headers=headers, params=parameters)
    response.raise_for_status()
    data = response.json()["data"]
    rows = []
    for coin_data in data:
        row = coin_data.copy()
        quote = row.pop('quote')
        for currency, quote_values in quote.items():
            for key, value in quote_values.items():
                row[f"{currency}_{key}"] = value
        rows.append(row)
    df=pd.DataFrame(rows)
    new_df=df[['name', 'id', 'symbol', 'slug', 'USD_price', 'USD_volume_24h', 'USD_percent_change_7d', 'USD_percent_change_30d', 'USD_market_cap']]
    new_df.to_sql("exercise_4_0_table", postgres_connection, schema="public", if_exists="replace", index=False)

postgres_connection = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
get_listing()