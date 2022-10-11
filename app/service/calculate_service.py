from app.models.calculate import Recipe, Energy, Portion
from app.service.tabela_service import TabelaService


def calculate_from_recipe(recipe: Recipe):
    recipe_add = recipe.receita
    final_height = recipe.peso_final

    diary_energy = 2000
    diary_carbohydrate = 300
    diary_protein = 75
    diary_total_fat = 55
    diary_saturated_fat = 22
    diary_fiber = 25
    diary_sodium = 2400

    total_carbohydrate = []
    total_protein = []
    total_total_fat = []
    total_saturated_fat = []
    total_trans_fat = []
    total_fiber = []
    total_sodium = []
    total_quantity = []

    for ingredient in recipe_add:
        ingredients_search = TabelaService().get_description(ingredient.ingrediente)
        quantity = ingredient.quantidade
        total_quantity.append(quantity)
        if ingredients_search.get('carbohydrate_g') == "":
            carbohydrate = 0
        else:
            carbohydrate = quantity * (float(ingredients_search.get('carbohydrate_g') / 100))
        total_carbohydrate.append(carbohydrate)
        if ingredients_search.get('protein_g') == "":
            protein = 0
        else:
            protein = quantity * (float(ingredients_search.get('protein_g') / 100))
        total_protein.append(protein)
        if ingredients_search.get('lipidius_g') == "":
            total_fat = 0
        else:
            total_fat = quantity * (float(ingredients_search.get('lipidius_g') / 100))
        total_total_fat.append(total_fat)
        if ingredients_search.get('saturated_g') == "":
            saturated_fat = 0
        else:
            saturated_fat = quantity * (float(ingredients_search.get('saturated_g') / 100))
        total_saturated_fat.append(saturated_fat)
        if ingredients_search.get('triglycerides') == "":
            trans_fat = 0
        else:
            trans_fat = quantity * (float(ingredients_search.get('triglycerides_g') / 100))
        total_trans_fat.append(trans_fat)
        if ingredients_search.get('fiber_g') == "":
            fiber = 0
        else:
            fiber = quantity * (float(ingredients_search.get('fiber_g') / 100))
        total_fiber.append(fiber)
        if ingredients_search.get('sodium_mg') == "":
            sodium = 0
        else:
            sodium = quantity * (float(ingredients_search.get('sodium_mg') / 100))
        total_sodium.append(sodium)

    table_carbohydrate = round(sum(total_carbohydrate) / final_height * recipe.porcao)
    table_protein = round(sum(total_protein) / final_height * recipe.porcao, 1)
    table_total_fat = round(sum(total_total_fat) / final_height * recipe.porcao, 1)
    table_energy = round((table_carbohydrate * 4) + (table_protein * 4) + (table_total_fat * 9))
    table_saturated_fat = round(sum(total_saturated_fat) / final_height * recipe.porcao, 1)
    table_trans_fat = round(sum(total_trans_fat) / final_height * recipe.porcao, 1)
    table_fiber = round(sum(total_fiber) / final_height * recipe.porcao, 1)
    table_sodium = round(sum(total_sodium) / final_height * recipe.porcao)

    diary_value_energy = table_energy * 100 / diary_energy
    diary_value_carbohydrate = table_carbohydrate * 100 / diary_carbohydrate
    diary_value_protein = table_protein * 100 / diary_protein
    diary_value_total_fat = table_total_fat * 100 / diary_total_fat
    diary_value_saturated_fat = table_saturated_fat * 100 / diary_saturated_fat
    diary_value_fiber = table_fiber * 100 / diary_fiber
    diary_value_sodium = table_sodium * 100 / diary_sodium

    return {
        "Quantidade": {
            "Energia": f"{table_energy}kcal",
            "Carboidrato": f"{table_carbohydrate}g",
            "Proteina": f"{table_protein}g",
            "Gordura_Total": f"{table_total_fat}g",
            "Gordura_Saturada": f"{table_saturated_fat}g",
            "Gordura_trans": f"{table_trans_fat}g",
            "Fibra": f"{table_fiber}g",
            "Sodio": f"{table_sodium}mg",
        },
        "%VD": {
            "Energia": f"{round(diary_value_energy)}%",
            "Carboidrato": f"{round(diary_value_carbohydrate)}%",
            "Proteina": f"{round(diary_value_protein)}%",
            "Gordura_Total": f"{round(diary_value_total_fat)}%",
            "Gordura_Saturada": f"{round(diary_value_saturated_fat)}%",
            "Gordura_Trans": f"Valor Diário não estabelecido",
            "Fibra": f"{round(diary_value_fiber)}%",
            "Sodio": f"{round(diary_value_sodium)}%",
        }
    }


def calculate_energy_for_recipe(energy: Energy):
    recipe_add = energy.receita

    total_carbohydrate = []
    total_protein = []
    total_total_fat = []
    total_quantity = []

    for ingredient in recipe_add:
        ingredient_search = TabelaService().get_description(ingredient.ingrediente)
        quantity = ingredient.quantidade
        total_quantity.append(quantity)
        if ingredient_search.get('carbohydrate_g') == "":
            carbohydrate = 0
        else:
            carbohydrate = quantity * (float(ingredient_search.get('carbohydrate_g') / 100))
        total_carbohydrate.append(carbohydrate)
        if ingredient_search.get('protein_g') == "":
            protein = 0
        else:
            protein = quantity * (float(ingredient_search.get('protein_g') / 100))
        total_protein.append(protein)
        if ingredient_search.get('lipidius_g') == "":
            total_fat = 0
        else:
            total_fat = quantity * (float(ingredient_search.get('lipidius_g') / 100))
        total_total_fat.append(total_fat)

    table_carbohydrate = sum(total_carbohydrate) / sum(total_quantity) * 100
    table_protein = sum(total_protein) / sum(total_quantity) * 100
    table_total_fat = sum(total_total_fat) / sum(total_quantity) * 100
    table_energy = (table_carbohydrate * 4) + (table_protein * 4) + (table_total_fat * 9)

    return {
        "Energia": f"{'{0:.3f}'.format(table_energy)}kcal"
    }


def calculate_portion_for_receipe(portion: Portion):
    portion_total = 100 * (float(portion.energia_media / portion.energia_receita))

    return {
        "Porcao": f"{'{0:.3f}'.format(portion_total)}g"
    }
