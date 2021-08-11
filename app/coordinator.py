import uvicorn

from app.utils.logger import logger
from app.service.endpoints import FastAPI, app


class Coordinator:
    def __init__(self):
        self.app = FastAPI()
        self.can_execute = 0

    def run(self):
        uvicorn.run(app)
        logger.info("Finding food...")
