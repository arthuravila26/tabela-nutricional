import json
import os

from app.db.mongo_conn import MongoDB
from app.models.calculate import Receita
from app.models.tabela_nutricional import TabelaNutricional
from app.utils.exceptions import DescriptionNotFound


def calculate_from_recipe(receita: Receita):
    # ingrediente = TabelaNutricional.get_by_description(description)
    receipe = receita.receita
    for ingredient in receipe:
        return f'{ingredient.ingrediente}: {ingredient.quantidade}'
