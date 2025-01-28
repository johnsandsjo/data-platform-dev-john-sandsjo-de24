from pathlib import Path
import json
from quixstreams import Application

#Now do similar outputs as in exercise 1 but using a producer to produce the data to a topic in 
#Kafka and then consuming the data. In the consumer, you will process the data to print out similar to above.

data_path = Path(__file__).parent / "data"

with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)


app = Application(broker_address="localhost:9092", consumer_group="orders_data")

order_topic = app.topic(name="orders", value_serializer="json")


def main():
    with app.get_producer() as producer:
        for order in orders:
            kafka_msg = order_topic.serialize(key=order["order_id"], value=order)
            print(f"Produced message: key = {kafka_msg.key}, value = {kafka_msg.value}")
            producer.produce(
                topic="orders", key=str(kafka_msg.key), value=kafka_msg.value
            )


# run this code only when executing this script and not when importing the module
if __name__ == "__main__":
    # pprint(jokes)
    main()