from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.database.base import Base


class AtributoProduto(Base):

    __tablename__ = "atributos"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    produto_id: Mapped[int] = mapped_column(
         ForeignKey("produtos.id")
    )


    nome: Mapped[str] = mapped_column(
        String(100)
    )


    valor: Mapped[str] = mapped_column(
        String(100)
    )