from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tfu.database import Base


class Categorias(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(20), unique=True)
    descricao: Mapped[Optional[str]] = mapped_column(Text)

    # ---------------- LIGAÇÕES (RELACIONAMENTOS) ---------------- #

    produtos: Mapped[list["Produtos"]] = relationship(
        back_populates="categoria", 
        cascade="all, delete-orphan"
    )