from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
import tempfile

from app.database.connection import get_db

from app.services.edital_service import (
    extrair_texto
)

from app.services.ia_service import (
    analisar_edital_ia
)

from app.services.produto_service import (
    buscar_ou_criar_produto
)

from app.services.atributo_service import (
    criar_atributo
)

from app.services.analise_service import (
    listar_analises
)

from app.services.comparacao_service import (
    comparar_produtos
)

from app.services.busca_produtos_service import (
    buscar_produto
)

router = APIRouter()


@router.post("/edital")
async def enviar_edital(
    arquivo: UploadFile,
    db: Session = Depends(get_db)
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        conteudo = await arquivo.read()

        temp.write(conteudo)

        caminho_pdf = temp.name


    texto = extrair_texto(
        caminho_pdf
    )


    dados = analisar_edital_ia(
        texto
    )


    produtos_encontrados = buscar_produto(

        dados["produto"]
    )


    for produto_externo in produtos_encontrados:

        produto = buscar_ou_criar_produto(

            db,

            produto_externo["nome"],

            produto_externo["preco"]
        )


        for nome, valor in produto_externo[
            "atributos"
        ].items():

            criar_atributo(

                db,

                produto.id,

                nome,

                valor
            )


    ranking = comparar_produtos(

        db,

        dados["requisitos"]
    )


    return {

        "analise": dados,

        "ranking": ranking
    }


@router.get("/analises")
def buscar_analises(
    db: Session = Depends(get_db)
):

    return listar_analises(
        db
    )