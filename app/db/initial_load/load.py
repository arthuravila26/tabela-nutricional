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
            file = os.path.join(dir_path, 'TabelaNutricional', 'test.json')
            with open(file) as json_file:
                data = json.load(json_file)
                for i in data:
                    table = TabelaNutricional()
                    table.id = i[0]
                    table.table.description = i[1]
                    table.category = i[2]
                    table.humidity_percents = i[3]
                    table.energy_kcal = i[4]
                    table.energy_kj = i[5]
                    table.lipidius_g = i[6]
                    table.cholesterol_mg = i[7]
                    table.carbohydrate_g = i[8]
                    table.fiber_g = i[9]
                    table.ashes_g = i[10]
                    table.calcium_mg = i[11]
                    table.magnesium_mg = i[12]
                    table.manganese_mg = i[13]
                    table.phosphorus_mg = i[14]
                    table.iron_mg = i[15]
                    table.sodium_mg = i[16]
                    table.potassium_mg = i[17]
                    table.copper_mg = i[18]
                    table.zinc_mg = i[19]
                    table.retinol_mcg = i[20]
                    table.re_mcg = i[21]
                    table.rae_mcg = i[22]
                    table.tiamina_mg = i[23]
                    table.riboflavin_mg = i[24]
                    table.pyridoxine_mg = i[25]
                    table.niacin_mg = i[26]
                    table.vitaminC_mg = i[27]
                    table.saturated_g = i[28]
                    table.monounsaturated_g = i[29]
                    table.polyunsaturated_g = i[30]
                    table.n12_0_g = i[31]
                    table.n14_0_g = i[32]
                    table.n16_0_g = i[33]
                    table.n18_0_g = i[34]
                    table.n20_0_g = i[35]
                    table.n22_0_g = i[36]
                    table.n24_0_g = i[37]
                    table.n14_1_g = i[38]
                    table.n16_1_g = i[39]
                    table.n18_1_g = i[40]
                    table.n20_1_g = i[41]
                    table.n18_2_n_6_g = i[42]
                    table.n18_3_n_3_g = i[43]
                    table.n20_4_g = i[44]
                    table.n20_5_g = i[45]
                    table.n22_5_g = i[46]
                    table.n22_6_g = i[47]
                    table.n18_1t_g = i[48]
                    table.n18_2t_g = i[49]
                    table.tryptophan_g = i[50]
                    table.threonine_g = i[51]
                    table.isoleucine_g = i[52]
                    table.leucine_g = i[53]
                    table.lysine_g = i[54]
                    table.methionine_g = i[55]
                    table.cystine_g = i[56]
                    table.phenylalanine_g = i[57]
                    table.tyrosine_g = i[58]
                    table.valine_g = i[59]
                    table.arginine_g = i[60]
                    table.histidine_g = i[61]
                    table.alanine_g = i[62]
                    table.aspartic_g = i[63]
                    table.glutamic_g = i[64]
                    table.glycine_g = i[65]
                    table.proline_g = i[66]
                    table.serine_g = i[67]
                    table.save()
        else:
            logger.info('Table already populated.')