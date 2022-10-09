from typing import List
from pydantic import BaseModel


class Ingredients(BaseModel):
    ingrediente: str
    quantidade: int


class Recipe(BaseModel):
    porcao: int
    peso_final: int
    receita: List[Ingredients]


class Portion(BaseModel):
    energia_receita: int
    energia_media: int


class Energy(BaseModel):
    receita: List[Ingredients]
