import json
import os


from app.db.mongo_conn import MongoDB
from app.models.calculate import Recipe
from app.models.tabela_nutricional import TabelaNutricional
from app.service.tabela_service import TabelaService
from app.utils.exceptions import DescriptionNotFound

'''
O item de receita recebido do POST da API vai ser inserido da seguite forma:
[Ingredients(ingredients='arroz_tipo_1_cozido', quantity=1.5), Ingredients(ingredients='arroz_tipo_1_cru', quantity=1.5)]
'''


def calculate_from_recipe(recipe: Recipe):
    recipe_add = recipe.recipe
    receipe_list = []
    for ingredient in recipe_add:
        ingredients_search = TabelaService().get_description(ingredient.ingredients)
        get_protein = ingredients_search.get('protein_g')
        quantity = ingredient.quantity
        result = quantity + get_protein
        print(result)
        receipe_list.append(result)
    return receipe_list
