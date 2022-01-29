import os
import mongoengine

from app.utils.logger import logger


class MongoConfigs:
    MONGODB_URI = os.getenv('MONGODB_URI')

    def __init__(self):
        self.__validate_uri()

    def __validate_uri(self, host=None):
        if self.MONGODB_URI is None and host is None:
            raise ValueError('MONGODB_URI should not be empty.')


class MongoDB:
    def __init__(self):
        self.settings = MongoConfigs()
        self.__connection()

    def __connection(self):
        logger.debug('Connecting to MongoDB')
        mongoengine.connection(host=MongoConfigs.MONGODB_URI)
        logger.debug('Connected to Mongo')
