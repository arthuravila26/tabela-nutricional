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
    def __init__(self, host=None):
        self.host = host
        self.__set_connection()

    def __set_connection(self):
        logger.debug('Connecting to Mongo')
        host = self.host if self.host else MongoConfigs.MONGODB_URI
        mongoengine.connect(host=host)
        logger.debug('Connected to Mongo')
