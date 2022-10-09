from mongoengine import Document, StringField, queryset_manager, IntField, DynamicField


class TabelaNutricional(Document):
    description = StringField(required=True)
    carbohydrate_g = DynamicField(required=True)
    protein_g = DynamicField(required=True)
    lipidius_g = DynamicField(required=True)
    saturated_g = DynamicField(required=True)
    fiber_g = DynamicField(required=True)
    sodium_mg = DynamicField(required=True)
    triglycerides_g = DynamicField(required=True)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    @queryset_manager
    def get_by_description(doc_cls, queryset, description):
        nutriente = queryset(description=str(description)).get()
        return nutriente

    def get_all(self):
        return TabelaNutricional.objects().all()

    meta = {
        'tabela_nutricional': 'tabela_nutricional'
    }
