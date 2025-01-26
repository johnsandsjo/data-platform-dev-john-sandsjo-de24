from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter",
    auto_offset_reset="earliest",
)

jokes_topic = app.topic(name="jokes", value_deserializer="json")


sdf = app.dataframe(topic=jokes_topic)


sdf = sdf.update(lambda message: print(f"Input: {message}"))

sdf = sdf.apply(lambda message: [{"word": word} for word in message["joke_text"].split()], expand=True)

sdf["lenght"] = sdf["word"].apply(lambda word: len(word))

sdf = sdf.update(lambda row: print(f"Output: {row}"))


if __name__ == "__main__":
    app.run()