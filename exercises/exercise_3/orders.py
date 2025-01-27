from pathlib import Path
import json
from pprint import pprint

data_path = Path(__file__).parent / "data"

with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)

total = 0
for order in orders:
    print(f"Input: {order}")
    for product in order["products"]:
        quant_price = product["quantity"]*product["price"]
        print(f"Product: {product["name"]}      Quantity: {product["quantity"]}     Price: {quant_price}")
        total += quant_price
    print(f"{total:.2f}")
    total = 0
    print()