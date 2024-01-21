from pydantic import  Field, PositiveFloat
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Centro de Treinamento', example='CT Big', max_length= 20)]
    endereco: Annotated[str, Field(description='Endereco do CT ', example='Rua A, 08', max_length= 60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario CT', example='CT Big', max_length= 30)]