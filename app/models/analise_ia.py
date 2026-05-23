from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AnaliseIA(Base):

    __tablename__ = "analises_ia"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    resultado: Mapped[str] = mapped_column(
        String(3000)
    )