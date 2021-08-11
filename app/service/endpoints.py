import json

from fastapi import FastAPI


app = FastAPI()

@app.get('/food')
def find_food(description):
    with open("lista-combinada.json") as read_file:
        data = json.load(read_file)

    for i in data:
        if i['description'] == 'Arroz, integral, cozido':
            print(i['category'])
