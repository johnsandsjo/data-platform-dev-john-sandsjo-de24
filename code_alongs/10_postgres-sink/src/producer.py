from quixstreams import Application
from constants import COINMARKET_API
from requests import Session
import json
from pprint import pprint
import time

API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def get_latest_coint_data(target_symbol = 'BTC'):
    parameters = {
    'symbol':target_symbol,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(API_URL, params=parameters)
    return json.loads(response.text)["data"][target_symbol]

def main():
    app = Application(broker_address="localhost:9092", consumer_group="coin_group")
    coint_topic = app.topic(name="coins", value_serializer="json")

    with app.get_producer() as producder:
        while True:
            coin_latest = get_latest_coint_data("BTC")
            kafka_message = coint_topic.serialize(key=coin_latest["symbol"], value=coin_latest)

            print(f"produce event with key = BTC, price = {coin_latest['quote']['USD']['price']}")

            producder.produce(topic=coint_topic.name, key=kafka_message.key, value=kafka_message.value)
            time.sleep(10)

if __name__== '__main__':
    #coint_data = get_latest_coint_data()
    #pprint(coint_data)
    main()