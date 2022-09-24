import json
from fastapi import Body, FastAPI
from starlette.responses import JSONResponse

from app.service.calculate_service import calculate_from_recipe, \
    calculate_portion_for_receipe, calculate_energy_for_recipe
from app.service.tabela_service import TabelaService
from app.models.calculate import Recipe, Energy, Portion

app = FastAPI()


@app.get('/tabelas', status_code=200)
def get_all_descriptions():
    return TabelaService().get_all_table()


@app.get('/{description}', status_code=200)
def get_description(description: str):
    description = description.split('&')
    data = {}
    for i in description:
        d = TabelaService().get_description(i)
        data[i] = d
    return JSONResponse(data)


@app.post('/calculo_rotulagem', status_code=200)
def calculate_table(recipe: Recipe):
    return calculate_from_recipe(recipe)


@app.post('/calculo_energia', status_code=200)
def calculate_energy(energy: Energy):
    return calculate_energy_for_recipe(energy)


@app.post('/calculo_porcao', status_code=200)
def calculate_portion(portion: Portion):
    return calculate_portion_for_receipe(portion)
