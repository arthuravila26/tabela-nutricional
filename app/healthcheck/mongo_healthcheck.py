from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from app.db.mongo_conn import MongoConfigs
from app.utils.logger import logger


def mongo_healthcheck():
    conn = MongoClient(f'{MongoConfigs.MONGODB_URI}', serverSelectionTimeoutMS=10000, connectTimeoutMS=10000)
    try:
        info = conn.server_info()
        return True
    except ServerSelectionTimeoutError:
        logger.critical("MongoDB is down.")
        return False
