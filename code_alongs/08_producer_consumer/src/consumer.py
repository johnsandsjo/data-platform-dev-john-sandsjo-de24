from quixstreams import Application

app = Application(broker_address= "localhost:9092", consumer_group= "text-splitter", auto_offset_reset="earliest")

jokes_topic = app.topic(name="jokes", value_deserializer="json")

#detta är inte en pandas dataframe, en annan typ av dataframe. Streaming data frame
sdf = app.dataframe(topic=jokes_topic)

sdf.update(lambda message: print(f"Input message: {message} \n"))

# detta är motsvarande för lamda funktionen ovan
#def print_message(message):
#   print(message)
#self.update(print_message)

#nu gör vi en transformation. Vill splita mellan orden (bara för test)
def split_words(message):
    return [{"word": word} for word in message["joke_text"].split()]

sdf = sdf.apply(split_words, expand=True)

sdf["length"] = sdf["word"].apply(lambda word: len(word))

sdf.update(lambda row: print(f"Output: {row}"))

if __name__ == '__main__':
    app.run()