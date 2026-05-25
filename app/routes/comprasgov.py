from fastapi import APIRouter
from typing import Optional

from app.services.comprasgov_service import (
    buscar_pregoes
)

router = APIRouter()


@router.get("/pregoes-governo")
def consultar(

    cidade: Optional[str] = None

):

    return buscar_pregoes(
        cidade
    )