import json
import os

from app.models.tabela_nutricional import TabelaNutricional
from app.utils.exceptions import DescriptionNotFound


class TabelaService:
    def serialize_calculate(self, data):
        return {
            "description": str(data.id),
            "quantity": data.quantity,
        }
