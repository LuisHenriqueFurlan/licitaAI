from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.busca_produtos_service import (
    buscar_produto
)

from app.services.produto_service import (
    buscar_ou_criar_produto
)

router = APIRouter()


@router.get("/buscar/{nome_produto}")
def buscar(
    nome_produto: str,
    db: Session = Depends(get_db)
):

    resultados = buscar_produto(
        nome_produto
    )


    produtos_salvos = []


    for produto in resultados:

        produto_salvo = buscar_ou_criar_produto(

            db,

            produto["nome"],

            int(produto["preco"])

        )


        produtos_salvos.append(
            produto_salvo
        )


    return produtos_salvos