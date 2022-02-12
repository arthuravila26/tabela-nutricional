import json
import os


class TabelaService:
    def __init__(self):
        file = os.path.join('app/db/initial_load/lista-combinada.json')
        with open(file) as json_file:
            self.data = json.load(json_file)

    def get_all(self):
        for i in self.data:
            return i
