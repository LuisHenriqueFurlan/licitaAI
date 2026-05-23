from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Pregao(Base):

    __tablename__ = "pregoes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    produto: Mapped[str] = mapped_column(
        String(100)
    )

    valor_referencia: Mapped[int] = mapped_column(
        Integer
    )