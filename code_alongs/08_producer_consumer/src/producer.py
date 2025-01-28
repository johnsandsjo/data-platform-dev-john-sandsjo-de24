from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application


data_path = Path(__file__).parents[1] / "data"

#reads in jokes.json in absolute path (but relative typ)
with open(data_path / "jokes.json", "r") as file:
    jokes = json.load(file)

# pprint(jokes)

# här startar vi en applikation. Entry point för Kafka. 
#9092 är den som vår container är mappad mot (ports mapped to broker container 9092) Så att man kan prata med broker
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

# skapadae en topic som vi kallade jokes. serialisation gör om json objektet till ett format som kan skickas i kommunikation.
jokes_topic = app.topic(name="jokes", value_serializer="json")

# print(jokes_topic)

#här skapar vi vår prodcuer
#loopar genom json array och serialiserar
#producerar med .produce key och value
def main():
    with app.get_producer() as producer:
        # print(producer)
        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)
            print(f"Produced message: key = {kafka_msg.key}, value = {kafka_msg.value}")

            # dags att producera
            producer.produce(
                topic="jokes", key=str(kafka_msg.key), value=kafka_msg.value
            )


# run this code only when executing this script and not when importing the module
if __name__ == "__main__":
    # pprint(jokes)
    main()