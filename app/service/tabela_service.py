import json
from datetime import datetime
from uuid import uuid4

from app.utils.exceptions import DescriptionNotFound
from app.utils.logger import logger


class TabelaService:
    def __init__(self):
        with open("files/test.json") as file:
            self.tabela = json.load(file)

    def get_all(self):
        for i in self.tabela:
            return i
