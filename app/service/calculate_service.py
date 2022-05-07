import json
import os

from app.db.mongo_conn import MongoDB
from app.models.calculate import Receita
from app.models.tabela_nutricional import TabelaNutricional
from app.utils.exceptions import DescriptionNotFound


def calculate_from_recipe(receita: Receita):
    return receita
