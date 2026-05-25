from fastapi import APIRouter

from app.services.comprasgov_service import (
    buscar_pregoes
)

from app.services.cache_service import (
    salvar_pregoes,
    obter_pregoes
)

router = APIRouter()


@router.get(
    "/atualizar-pregoes"
)
def atualizar():

    dados = buscar_pregoes()

    salvar_pregoes(
        dados
    )

    return {

        "mensagem":
        "Pregões atualizados",

        "total":
        dados.get(
            "total_pregoes",
            0
        )

    }


@router.get(
    "/cache-pregoes"
)
def listar():

    return obter_pregoes()