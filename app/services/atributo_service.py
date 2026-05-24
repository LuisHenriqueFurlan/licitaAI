from sqlalchemy.orm import Session

from app.models.atributo_produto import (
    AtributoProduto
)


def criar_atributo(
    db: Session,
    produto_id: int,
    nome: str,
    valor: str
):

    novo_atributo = AtributoProduto(

        produto_id=produto_id,

        nome=nome,

        valor=valor
    )


    db.add(
        novo_atributo
    )

    db.commit()

    db.refresh(
        novo_atributo
    )

    return novo_atributo

def listar_atributos(
    db: Session,
    produto_id: int
):

    return db.query(
        AtributoProduto
    ).filter(
        AtributoProduto.produto_id == produto_id
    ).all()