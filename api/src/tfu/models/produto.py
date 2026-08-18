from decimal import Decimal
from typing import Optional

from sqlalchemy import ForeignKey, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tfu.database import Base


class Produtos(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False) 
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) 
    estoque: Mapped[int] = mapped_column()
    descricao: Mapped[Optional[str]] = mapped_column(Text)

    # ---------------- LIGAÇÕES (RELACIONAMENTOS) ---------------- #

  
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False)
    categoria: Mapped["Categorias"] = relationship(back_populates="produtos")

   
    pedidos: Mapped[list["Pedidos"]] = relationship(
        secondary="pedido_produto", 
        back_populates="produtos"
    )