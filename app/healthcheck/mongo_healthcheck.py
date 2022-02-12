import os

import mongoengine

from app.utils.logger import logger


def mongo_healthcheck():
    try:
        client = mongoengine.connect(host=os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000)
        client.server_info()
        return True
    except mongoengine.ConnectionFailure:
        logger.error(f"Connection Failure with database")
        return False
    except Exception as e:
        logger.error(f"Something happend in connect db {e.args}")
        return False