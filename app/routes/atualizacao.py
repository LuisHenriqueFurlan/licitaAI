from fastapi import APIRouter

from app.services.comprasgov_service import (
    buscar_pregoes
)

from app.services.database_service import (
    salvar_pregao,
    listar_pregoes
)

router = APIRouter()


@router.get(
    "/atualizar-pregoes"
)
def atualizar():

    dados = buscar_pregoes()


    for pregao in dados.get(
        "pregoes",
        []
    ):

        salvar_pregao(
            pregao
        )


    return {

        "mensagem":
        "Pregões salvos",

        "total":
        len(
            dados.get(
                "pregoes",
                []
            )
        )

    }


@router.get(
    "/historico-pregoes"
)
def historico():

    return listar_pregoes()