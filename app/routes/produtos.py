from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.produto_schema import ProdutoCreate
from app.services.produto_service import (
    criar_produto,
    listar_produtos
)
from app.schemas.produto_schema import (
    ProdutoCreate,
    CompararProduto
)

from app.services.produto_service import (
    criar_produto,
    listar_produtos,
    comparar_produtos
)

from app.schemas.comparacao_schema import (
    ComparacaoRequest
)

from app.services.produto_service import (
    criar_produto,
    listar_produtos,
    comparar_produtos,
    comparar_requisitos
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

@router.post("/comparar")
def comparar(
    dados: CompararProduto,
    db: Session = Depends(get_db)
):

    return comparar_produtos(
        db,
        dados.preco_maximo
    )

@router.post("/comparar-requisitos")
def comparar_por_requisitos(
    dados: ComparacaoRequest,
    db: Session = Depends(get_db)
):

    return comparar_requisitos(
        db,
        dados.preco_maximo,
        dados.requisitos
    )