from fastapi import FastAPI
from starlette.responses import JSONResponse

from app.service.tabela_service import TabelaService

app = FastAPI()


@app.get('/tabelas', status_code=200)
def get_todas_descrições():
    return TabelaService().get_all()
