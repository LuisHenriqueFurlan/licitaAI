from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.atributo_schema import (
    AtributoCreate
)

from app.services.atributo_service import (
    criar_atributo
)

from app.services.atributo_service import (
    criar_atributo,
    listar_atributos
)

router = APIRouter()


@router.post("/atributos")
def cadastrar_atributo(
    atributo: AtributoCreate,
    db: Session = Depends(get_db)
):

    return criar_atributo(
        db,
        atributo.produto_id,
        atributo.nome,
        atributo.valor
    )

@router.get("/produtos/{produto_id}/atributos")
def buscar_atributos(
    produto_id: int,
    db: Session = Depends(get_db)
):

    return listar_atributos(
        db,
        produto_id
    )