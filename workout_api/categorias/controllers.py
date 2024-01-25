from uuid import uuid4
from fastapi import APIRouter, status, Body
from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DatabeseDependency
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut


router = APIRouter()


@router.post('/', 
             summary='Criar uma nova Categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CategoriaOut,)

async def post(
    db_sesseion: DatabeseDependency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_sesseion.add(categoria_model)
    await db_sesseion.commit()
    return categoria_out
