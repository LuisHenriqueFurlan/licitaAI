from fastapi import APIRouter

from app.services.comprasgov_service import (
    buscar_pregoes
)

router = APIRouter()


@router.get("/pregoes-governo")
def consultar(

    cidade: str = None,
    uasg: int = None

):

    return buscar_pregoes(

        cidade,
        uasg

    )