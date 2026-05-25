from fastapi import APIRouter, UploadFile, File
from app.services.edital_service import processar_edital

router = APIRouter()


@router.post("/upload-edital")
async def upload_edital(
    arquivo: UploadFile = File(...)
):

    resultado = await processar_edital(
        arquivo
    )

    return resultado