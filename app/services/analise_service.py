from sqlalchemy.orm import Session

from app.models.analise_ia import AnaliseIA


def salvar_analise(
    db: Session,
    resultado: str
):

    nova_analise = AnaliseIA(
        resultado=resultado
    )

    db.add(
        nova_analise
    )

    db.commit()

    db.refresh(
        nova_analise
    )

    return nova_analise


def listar_analises(
    db: Session
):

    return db.query(
        AnaliseIA
    ).all()