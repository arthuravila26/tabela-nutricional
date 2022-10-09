import json
import os
import mongoengine

from app.models.tabela_nutricional import TabelaNutricional
from app.utils.logger import logger


class InitialLoad:
    @staticmethod
    def connect():
        mongoengine.connect(host=os.getenv('MONGO_URI'))

    def create_objects(self):
        self.load_table()

    def load_table(self):
        if TabelaNutricional.objects.count() == 0:
            logger.info('Populating nutritional table with nutritional values.')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file = os.path.join(dir_path, 'test.json')
            with open(file) as json_file:
                data = json.load(json_file)
                for i in data:
                    table = TabelaNutricional(
                        description=i['description'],
                        carbohydrate_g=i['carbohydrate_g'],
                        protein_g=i['protein_g'],
                        lipidius_g=i['lipidius_g'],
                        saturated_g=i['saturated_g'],
                        fiber_g=i['fiber_g'],
                        sodium_mg=i['sodium_mg'],
                        triglycerides_g=i['triglycerides_g']
                    )
                    table.save()
        else:
            logger.info('Table already populated.')
