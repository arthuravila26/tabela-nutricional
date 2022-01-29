from fastapi import HTTPException


class DescriptionNotFound(HTTPException):
    def __init__(self, msg: str = 'Alimento não encontrado.'):
        super().__init__(detail=msg, status_code=422)


class MongoDBDown(HTTPException):
    def __init__(self, msg: str = 'Banco de dados fora do ar.'):
        super().__init__(detail=msg, status_code=500)
