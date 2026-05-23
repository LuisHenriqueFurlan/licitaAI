from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
import tempfile

from app.database.connection import get_db
from app.services.edital_service import extrair_texto
from app.services.ia_service import analisar_edital
from app.services.analise_service import salvar_analise
from app.services.analise_service import (
    salvar_analise,
    listar_analises
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


    analise = analisar_edital(
        texto
    )


    salvar_analise(
        db,
        analise
    )


    return {
        "analise": analise
    }

@router.get("/analises")
def buscar_analises(
    db: Session = Depends(get_db)
):

    return listar_analises(
        db
    )