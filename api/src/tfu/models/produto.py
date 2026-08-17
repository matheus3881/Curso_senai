

    

from decimal import Decimal
from typing import Optional

from sqlalchemy import Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from tfu.database import Base


class Produtos(Base):

    __tablename__ = "produtos"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False) 
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) 
    estoque: Mapped[int] = mapped_column()
    descricao: Mapped[Optional[str]] = mapped_column(Text)