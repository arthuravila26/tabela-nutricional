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
            file = os.path.join(dir_path, 'lista-combinada.json')
            with open(file) as json_file:
                data = json.load(json_file)
                for i in data:
                    table = TabelaNutricional(description=i['description'],
                                              category=i['category'],
                                              humidity_percents=i['humidity_percents'],
                                              energy_kcal=i['energy_kcal'],
                                              energy_kj=i['energy_kj'],
                                              protein_g=i['protein_g'],
                                              lipidius_g=i['lipidius_g'],
                                              cholesterol_mg=i['cholesterol_mg'],
                                              carbohydrate_g=i['carbohydrate_g'],
                                              fiber_g=i['fiber_g'],
                                              ashes_g=i['ashes_g'],
                                              calcium_mg=i['calcium_mg'],
                                              magnesium_mg=i['magnesium_mg'],
                                              manganese_mg=i['manganese_mg'],
                                              phosphorus_mg=i['phosphorus_mg'],
                                              iron_mg=i['iron_mg'],
                                              sodium_mg=i['sodium_mg'],
                                              potassium_mg=i['potassium_mg'],
                                              copper_mg=i['copper_mg'],
                                              zinc_mg=i['zinc_mg'],
                                              retinol_mcg=i['retinol_mcg'],
                                              re_mcg=i['re_mcg'],
                                              rae_mcg=i['rae_mcg'],
                                              tiamina_mg=i['tiamina_mg'],
                                              riboflavin_mg=i['riboflavin_mg'],
                                              pyridoxine_mg=i['pyridoxine_mg'],
                                              niacin_mg=i['niacin_mg'],
                                              vitaminC_mg=i['vitaminC_mg'],
                                              saturated_g=i['saturated_g'],
                                              monounsaturated_g=i['monounsaturated_g'],
                                              polyunsaturated_g=i['polyunsaturated_g'],
                                              n12_0_g=i['12:0_g'],
                                              n14_0_g=i['14:0_g'],
                                              n16_0_g=i['16:0_g'],
                                              n18_0_g=i['18:0_g'],
                                              n20_0_g=i['20:0_g'],
                                              n22_0_g=i['22:0_g'],
                                              n24_0_g=i['24:0_g'],
                                              n14_1_g=i['14:1_g'],
                                              n16_1_g=i['16:1_g'],
                                              n18_1_g=i['18:1_g'],
                                              n20_1_g=i['20:1_g'],
                                              n18_2_n_6_g=i['18:2 n-6_g'],
                                              n18_3_n_3_g=i['18:3 n-3_g'],
                                              n20_4_g=i['20:4_g'],
                                              n20_5_g=i['20:5_g'],
                                              n22_5_g=i['22:5_g'],
                                              n22_6_g=i['22:6_g'],
                                              n18_1t_g=i['18:1t_g'],
                                              n18_2t_g=i['18:2t_g'],
                                              tryptophan_g=i['tryptophan_g'],
                                              threonine_g=i['threonine_g'],
                                              isoleucine_g=i['isoleucine_g'],
                                              leucine_g=i['leucine_g'],
                                              lysine_g=i['lysine_g'],
                                              methionine_g=i['methionine_g'],
                                              cystine_g=i['cystine_g'],
                                              phenylalanine_g=i['phenylalanine_g'],
                                              tyrosine_g=i['tyrosine_g'],
                                              valine_g=i['valine_g'],
                                              arginine_g=i['arginine_g'],
                                              histidine_g=i['histidine_g'],
                                              alanine_g=i['alanine_g'],
                                              aspartic_g=i['aspartic_g'],
                                              glutamic_g=i['glutamic_g'],
                                              glycine_g=i['glycine_g'],
                                              proline_g=i['proline_g'],
                                              serine_g=i['serine_g'])
                    table.save()
        else:
            logger.info('Table already populated.')
