import json
import sys

with open("foodlist.json") as file:
    # Load its content and make a new dictionary
    data = json.load(file)

    # Delete the "client" key-value pair from each order
    for i in data["alimentos"]:
        print(i["description"])
