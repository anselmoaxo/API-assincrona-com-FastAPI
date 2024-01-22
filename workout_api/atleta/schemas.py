from pydantic import Field
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', example='12345678912', max_length=11)]
    idade: Annotated[float, Field(description='idade do atleta', example=25)]
    peso: Annotated[float, Field(description='Peso do atleta', example=70.3)]
    altura: Annotated[float, Field(description='altura do atleta', example=1.60)]
    sexo: Annotated[str, Field(description='sexo do atleta', example='M')]
