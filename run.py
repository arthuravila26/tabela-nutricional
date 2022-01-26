from app.coordinator import Coordinator
# import json
# import sys
#
#
# def arquivo():
#     with open("files/test.json") as file:
#         # Load its content and make a new dictionary
#         data = json.load(file)
#
#         # Delete the "client" key-value pair from each order
#         for i in data:
#             print(i)

if __name__ == '__main__':
    c = Coordinator()
    c.run()
