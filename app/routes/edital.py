from fastapi import APIRouter, UploadFile
import tempfile

from app.services.edital_service import extrair_texto

router = APIRouter()


@router.post("/edital")
async def enviar_edital(
    arquivo: UploadFile
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

    return {
        "texto": texto[:1000]
    }