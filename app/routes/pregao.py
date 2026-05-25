from fastapi import APIRouter

from app.services.comprasgov_service import (
    buscar_pregoes
)

router = APIRouter()


@router.get(
    "/pregao/{pregao_id}"
)
def detalhe(
    pregao_id: str
):

    dados = buscar_pregoes()

    for p in dados.get(
        "pregoes",
        []
    ):

        if str(
            p["pregao_id"]
        ) == str(
            pregao_id
        ):

            return p


    return {

        "erro":
        "Pregão não encontrado"

    }