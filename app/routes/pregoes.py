from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.pregao_schema import PregaoCreate
from app.services.pregoes_service import (
    criar_pregao,
    listar_pregoes
)

router = APIRouter()


@router.post("/pregoes")
def cadastrar_pregao(
    pregao: PregaoCreate,
    db: Session = Depends(get_db)
):

    return criar_pregao(
        db,
        pregao.produto,
        pregao.valor_referencia
    )

@router.get("/pregoes")
def buscar_pregoes(
    db: Session = Depends(get_db)
):

    return listar_pregoes(db)