from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database.base import Base


class Produto(Base):

    __tablename__ = "produtos"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    nome: Mapped[str] = mapped_column(
        String(100)
    )


    preco: Mapped[int] = mapped_column(
        Integer
    )

    atributos = relationship(
    "AtributoProduto",
    backref="produto"
    )