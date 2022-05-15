from typing import List
from pydantic import BaseModel


class Ingredients(BaseModel):
    ingredients: str
    quantity: float


class Recipe(BaseModel):
    recipe: List[Ingredients]
