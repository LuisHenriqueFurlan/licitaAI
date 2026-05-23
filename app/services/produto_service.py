from sqlalchemy.orm import Session

from app.models.produto import Produto


def criar_produto(
    db: Session,
    nome: str,
    preco: int
):

    novo_produto = Produto(
        nome=nome,
        preco=preco
    )

    db.add(
        novo_produto
    )

    db.commit()

    db.refresh(
        novo_produto
    )

    return novo_produto


def listar_produtos(
    db: Session
):

    return db.query(
        Produto
    ).all()