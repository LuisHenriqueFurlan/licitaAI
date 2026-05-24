from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AtributoProduto(Base):

    __tablename__ = "atributos_produto"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    produto_id: Mapped[int] = mapped_column(
        Integer
    )


    nome: Mapped[str] = mapped_column(
        String(100)
    )


    valor: Mapped[str] = mapped_column(
        String(100)
    )