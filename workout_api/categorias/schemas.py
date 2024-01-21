from pydantic import  Field, PositiveFloat
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Categoria', example='Scale', max_length= 10)]