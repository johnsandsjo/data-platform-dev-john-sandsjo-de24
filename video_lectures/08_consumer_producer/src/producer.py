from quixstreams import Application
from pathlib import Path
import json
from pprint import pprint

app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

jokes_topic = app.topic(name="jokes", value_serializer="json")

jokes_path = Path(__file__).parents[1] / "data" / "jokes.json"


with open(jokes_path, "r", encoding="utf-8") as file:
    jokes = json.load(file)


def main():
    with app.get_producer() as producer:
        # print(producer)
        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)

            print(
                f"produce event with key = {kafka_msg.key}, value = {kafka_msg.value}"
            )
            producer.produce(
                topic=jokes_topic.name, key=str(kafka_msg.key), value= kafka_msg.value
                )


# pprint(jokes)

if __name__ == "__main__":
    main()
