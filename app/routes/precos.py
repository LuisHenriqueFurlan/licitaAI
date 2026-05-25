from fastapi import APIRouter

from app.services.preco_service import (
    buscar_menor_preco
)

router = APIRouter()


@router.get("/buscar-preco")
def buscar(produto: str):

    return buscar_menor_preco(
        produto
    )