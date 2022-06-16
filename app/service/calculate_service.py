from app.models.calculate import Recipe
from app.service.tabela_service import TabelaService


def calculate_from_recipe(recipe: Recipe):
    recipe_add = recipe.recipe

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
    total_fiber = []
    total_sodium = []
    total_quantity = []

    for ingredient in recipe_add:
        ingredients_search = TabelaService().get_description(ingredient.ingredients)
        quantity = ingredient.quantity
        total_quantity.append(quantity)
        if ingredients_search.get('carbohydrate_g') == "":
            carbohydrate = 0
        else:
            carbohydrate = quantity * (float("{:.2f}".format(ingredients_search.get('carbohydrate_g') / 100)))
        total_carbohydrate.append(carbohydrate)
        if ingredients_search.get('protein_g') == "":
            protein = 0
        else:
            protein = quantity * (float("{:.2f}".format(ingredients_search.get('protein_g') / 100)))
        total_protein.append(protein)
        if ingredients_search.get('lipidius_g') == "":
            total_fat = 0
        else:
            total_fat = quantity * (float("{:.2f}".format(ingredients_search.get('lipidius_g') / 100)))
        total_total_fat.append(total_fat)
        if ingredients_search.get('saturated_g') == "":
            saturated_fat = 0
        else:
            saturated_fat = quantity * (float("{:.2f}".format(ingredients_search.get('saturated_g') / 100)))
        total_saturated_fat.append(saturated_fat)
        if ingredients_search.get('fiber_g') == "":
            fiber = 0
        else:
            fiber = quantity * (float("{:.2f}".format(ingredients_search.get('fiber_g') / 100)))
        total_fiber.append(fiber)
        if ingredients_search.get('sodium_mg') == "":
            sodium = 0
        else:
            sodium = quantity * (float("{:.2f}".format(ingredients_search.get('sodium_mg') / 100)))
        total_sodium.append(sodium)

    table_carbohydrate = sum(total_carbohydrate) / sum(total_quantity) * recipe.portion
    table_protein = sum(total_protein) / sum(total_quantity) * recipe.portion
    table_total_fat = sum(total_total_fat) / sum(total_quantity) * recipe.portion
    table_energy = (table_carbohydrate * 4) + (table_protein * 4) + (table_total_fat * 9)
    table_saturated_fat = sum(total_saturated_fat) / sum(total_quantity) * recipe.portion
    table_fiber = sum(total_fiber) / sum(total_quantity) * recipe.portion
    table_sodium = sum(total_sodium) / sum(total_quantity) * recipe.portion

    diary_value_energy = table_energy * 100 / diary_energy
    diary_value_carbohydrate = table_carbohydrate * 100 / diary_carbohydrate
    diary_value_protein = table_protein * 100 / diary_protein
    diary_value_total_fat = table_total_fat * 100 / diary_total_fat
    diary_value_saturated_fat = table_saturated_fat * 100 / diary_saturated_fat
    diary_value_fiber = table_fiber * 100 / diary_fiber
    diary_value_sodium = table_sodium * 100 / diary_sodium

    return {
        "Quantity": {
            "Energy": f"{'{0:.2g}'.format(table_energy)}g",
            "Carbohydrate": f"{'{0:.2g}'.format(table_carbohydrate)}g",
            "Protein": f"{'{0:.2g}'.format(table_protein)}g",
            "Total_fat": f"{'{0:.2g}'.format(table_total_fat)}g",
            "Saturated_fat": f"{'{0:.2g}'.format(table_saturated_fat)}g",
            "Fiber": f"{'{0:.2g}'.format(table_fiber)}g",
            "Sodium": f"{'{0:.2g}'.format(table_sodium)}g",
        },
        "%VD": {
            "Energy": f"{'{0:.2g}'.format(diary_value_energy)}g",
            "Carbohydrate": f"{'{0:.2g}'.format(diary_value_carbohydrate)}g",
            "Protein": f"{'{0:.2g}'.format(diary_value_protein)}g",
            "Total_fat": f"{'{0:.2g}'.format(diary_value_total_fat)}g",
            "Saturated_fat": f"{'{0:.2g}'.format(diary_value_saturated_fat)}g",
            "Fiber": f"{'{0:.2g}'.format(diary_value_fiber)}g",
            "Sodium": f"{'{0:.2g}'.format(diary_value_sodium)}g",
        }
    }
