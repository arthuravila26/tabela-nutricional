import json
import os

from app.models.tabela_nutricional import TabelaNutricional


class TabelaService:
    def __init__(self):
        file = os.path.join('app/db/initial_load/lista-combinada.json')
        with open(file) as json_file:
            self.data = json.load(json_file)

    def get_all_table(self):
        table_json = [self.serialize(table) for table in TabelaNutricional().get_all()]
        return table_json

    def serialize(self, data):
        return {
            "id": str(data.id),
            "description": data.description,
            "category": data.category,
            "humidity_percents": data.humidity_percents,
            "energy_kcal": data.energy_kcal,
            "energy_kj": data.energy_kj,
            "protein_g": data.protein_g,
            "lipidius_g": data.lipidius_g,
            "cholesterol_mg": data.cholesterol_mg,
            "carbohydrate_g": data.carbohydrate_g,
            "fiber_g": data.fiber_g,
            "ashes_g": data.ashes_g,
            "calcium_mg": data.calcium_mg,
            "magnesium_mg": data.magnesium_mg,
            "manganese_mg": data.manganese_mg,
            "phosphorus_mg": data.phosphorus_mg,
            "iron_mg": data.iron_mg,
            "sodium_mg": data.sodium_mg,
            "potassium_mg": data.potassium_mg,
            "copper_mg": data.copper_mg,
            "zinc_mg": data.zinc_mg,
            "retinol_mcg": data.retinol_mcg,
            "re_mcg": data.re_mcg,
            "rae_mcg": data.rae_mcg,
            "tiamina_mg": data.tiamina_mg,
            "riboflavin_mg": data.riboflavin_mg,
            "pyridoxine_mg": data.pyridoxine_mg,
            "niacin_mg": data.niacin_mg,
            "vitaminC_mg": data.vitaminC_mg,
            "saturated_g": data.saturated_g,
            "monounsaturated_g": data.monounsaturated_g,
            "polyunsaturated_g": data.polyunsaturated_g,
            "12:0_g": data.n12_0_g,
            "14:0_g": data.n14_0_g,
            "16:0_g": data.n16_0_g,
            "18:0_g": data.n18_0_g,
            "20:0_g": data.n20_0_g,
            "22:0_g": data.n22_0_g,
            "24:0_g": data.n24_0_g,
            "14:1_g": data.n14_1_g,
            "16:1_g": data.n16_1_g,
            "18:1_g": data.n18_1_g,
            "20:1_g": data.n20_1_g,
            "18:2 n-6_g": data.n18_2_n_6_g,
            "18:3 n-3_g": data.n18_3_n_3_g,
            "20:4_g": data.n20_4_g,
            "20:5_g": data.n20_5_g,
            "22:5_g": data.n22_5_g,
            "22:6_g": data.n22_6_g,
            "18:1t_g": data.n18_1t_g,
            "18:2t_g": data.n18_2t_g,
            "tryptophan_g": data.tryptophan_g,
            "threonine_g": data.threonine_g,
            "isoleucine_g": data.isoleucine_g,
            "leucine_g": data.leucine_g,
            "lysine_g": data.lysine_g,
            "methionine_g": data.methionine_g,
            "cystine_g": data.cystine_g,
            "phenylalanine_g": data.phenylalanine_g,
            "tyrosine_g": data.tyrosine_g,
            "valine_g": data.valine_g,
            "arginine_g": data.arginine_g,
            "histidine_g": data.histidine_g,
            "alanine_g": data.alanine_g,
            "aspartic_g": data.aspartic_g,
            "glutamic_g": data.glutamic_g,
            "glycine_g": data.glycine_g,
            "proline_g": data.proline_g,
            "serine_g": data.serine_g
        }
