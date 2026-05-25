from fastapi import APIRouter

from app.services.mercado_service import (
    buscar_precos
)

router = APIRouter()


@router.get(
    "/mercado"
)
def consultar(
    produto:str
):

    return buscar_precos(
        produto
    )