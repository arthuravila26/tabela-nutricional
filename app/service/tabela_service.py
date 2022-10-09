import json
import os

from app.models.tabela_nutricional import TabelaNutricional
from app.utils.exceptions import DescriptionNotFound


class TabelaService:
    def get_all_table(self):
        table_json = [self.serialize_table(table) for table in TabelaNutricional().get_all()]
        return table_json

    def get_description(self, description):
        try:
            description = TabelaNutricional.get_by_description(description)
            return self.serialize_table(description)
        except:
            raise DescriptionNotFound

    def serialize_table(self, data):
        return {
            "id": str(data.id),
            "description": data.description,
            "carbohydrate_g": data.carbohydrate_g,
            "protein_g": data.protein_g,
            "lipidius_g": data.lipidius_g,
            "saturated_g": data.saturated_g,
            "fiber_g": data.fiber_g,
            "sodium_mg": data.sodium_mg,
            "triglycerides_g": data.triglycerides_g
        }
