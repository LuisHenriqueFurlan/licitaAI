from sqlalchemy.orm import Session

from app.models.pregao import Pregao


def criar_pregao(
    db: Session,
    produto: str,
    valor_referencia: int
):

    novo_pregao = Pregao(
        produto=produto,
        valor_referencia=valor_referencia
    )

    db.add(novo_pregao)

    db.commit()

    db.refresh(novo_pregao)

    return novo_pregao


def listar_pregoes(db: Session):

    return db.query(Pregao).all()