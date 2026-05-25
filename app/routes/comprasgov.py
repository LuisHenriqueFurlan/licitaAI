from fastapi import APIRouter
from app.services.comprasgov_service import buscar_pregoes

router = APIRouter()


@router.get("/pregoes-governo")
def consultar():

    return buscar_pregoes()