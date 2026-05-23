from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.produto_schema import ProdutoCreate
from app.services.produto_service import (
    criar_produto,
    listar_produtos
)

router = APIRouter()


@router.post("/produtos")
def cadastrar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):

    return criar_produto(
        db,
        produto.nome,
        produto.preco
    )


@router.get("/produtos")
def buscar_produtos(
    db: Session = Depends(get_db)
):

    return listar_produtos(
        db
    )