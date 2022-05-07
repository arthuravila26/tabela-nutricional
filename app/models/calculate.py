from typing import List
from pydantic import BaseModel


class Ingredientes(BaseModel):
    ingrediente: str
    quantidade: float


class Receita(BaseModel):
    receita: List[Ingredientes] = []
