from mongoengine import Document, StringField, queryset_manager, IntField


class TabelaNutricional(Document):
    id = IntField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    humidity_percents = IntField(required=True)
    energy_kcal = IntField(required=True)
    energy_kj = IntField(required=True)
    lipidius_g = IntField(required=True)
    cholesterol_mg = StringField(required=True)
    carbohydrate_g = IntField(required=True)
    fiber_g = IntField(required=True)
    ashes_g = IntField(required=True)
    calcium_mg = IntField(required=True)
    magnesium_mg = IntField(required=True)
    manganese_mg = IntField(required=True)
    phosphorus_mg = IntField(required=True)
    iron_mg = IntField(required=True)
    sodium_mg = IntField(required=True)
    potassium_mg = IntField(required=True)
    copper_mg = IntField(required=True)
    zinc_mg = IntField(required=True)
    retinol_mcg = StringField(required=True)
    re_mcg = StringField(required=False)
    rae_mcg = StringField(required=False)
    tiamina_mg = IntField(required=True)
    riboflavin_mg = StringField(required=True)
    pyridoxine_mg = IntField(required=True)
    niacin_mg = StringField(required=True)
    vitaminC_mg = StringField(required=False)
    saturated_g = IntField(required=True)
    monounsaturated_g = IntField(required=True)
    polyunsaturated_g = IntField(required=True)
    n12_0_g = StringField(required=False)
    n14_0_g = StringField(required=True)
    n16_0_g = IntField(required=True)
    n18_0_g = IntField(required=True)
    n20_0_g = StringField(required=True)
    n22_0_g = StringField(required=True)
    n24_0_g = StringField(required=True)
    n14_1_g = StringField(required=False)
    n16_1_g = StringField(required=False)
    n18_1_g = IntField(required=True)
    n20_1_g = StringField(required=True)
    n18_2_n_6_g = IntField(required=True)
    n18_3_n_3_g = IntField(required=True)
    n20_4_g = StringField(required=False)
    n20_5_g = StringField(required=False)
    n22_5_g = StringField(required=True)
    n22_6_g = StringField(required=False)
    n18_1t_g = StringField(required=False)
    n18_2t_g = StringField(required=False)
    tryptophan_g = StringField(required=False)
    threonine_g = StringField(required=False)
    isoleucine_g = StringField(required=False)
    leucine_g = StringField(required=False)
    lysine_g = StringField(required=False)
    methionine_g = StringField(required=False)
    cystine_g = StringField(required=False)
    phenylalanine_g = StringField(required=False)
    tyrosine_g = StringField(required=False)
    valine_g = StringField(required=False)
    arginine_g = StringField(required=False)
    histidine_g = StringField(required=False)
    alanine_g = StringField(required=False)
    aspartic_g = StringField(required=False)
    glutamic_g = StringField(required=False)
    glycine_g = StringField(required=False)
    proline_g = StringField(required=False)
    serine_g = StringField(required=False)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    @queryset_manager
    def get_by_description(doc_cls, queryset, description):
        nutriente = queryset(description=str(description)).first()
        return nutriente

    meta = {
        'tabela_nutricional': 'tabela_nutricional',
        'indexes': ['description']
    }
