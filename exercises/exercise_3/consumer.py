from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="orders_data",
    auto_offset_reset="earliest",
)

orders_topic = app.topic(name = "orders", value_deserializer="json")

sdf = app.dataframe(topic=orders_topic)

#sdf = sdf.update(lambda message: print(f"Input message: {message} \n"))

def print_order(message):
    total = 0
    print(f"Input: {message}")
    for product in message["products"]:
        quant_price = product["quantity"]*product["price"]
        print(f"Product: {product["name"]} Qunatity: {product["quantity"]} Price: {quant_price}")
        total += quant_price
    print(f"{total}")
    total = 0
    print()

sdf.update(print_order)

if __name__ == '__main__':
    app.run()