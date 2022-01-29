import uvicorn

from app.db.initial_load.load import InitialLoad
from app.db.mongo_conn import MongoDB
from app.main import FastAPI, app
from app.utils.logger import logger


class Coordinator:
    def __init__(self):
        self.app = FastAPI()
        self.mgdb = MongoDB()
        load = InitialLoad()
        load.create_objects()
        self.can_execute = 0

    def run(self):
        uvicorn.run(app)
        logger.info("Parando Tabela Nutricional...")
