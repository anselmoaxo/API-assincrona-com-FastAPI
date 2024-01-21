from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Joao', max_length= 50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', examples='12345678912', max_length= 11)]
    idade: Annotated[int, Field(description='idade do atleta', examples= 25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples= 70.3)]
    altura: Annotated[PositiveFloat, Field(description='altura do atleta', examples= 1.60)]
    sexo: Annotated[str, Field(description='sexo do atleta', examples='M')]