from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import (
    get_db
)

from app.schemas.comparacao_schema import (
    CompararProduto
)

from app.services.comparacao_service import (
    comparar_produtos
)

router = APIRouter()


@router.post(
    "/comparar-edital"
)
def comparar_edital(

    dados: CompararProduto,

    db: Session = Depends(
        get_db
    )
):

    resultados = comparar_produtos(

        db,

        dados.requisitos
    )

    return resultados