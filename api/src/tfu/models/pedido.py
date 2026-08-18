from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, Table, func
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tfu.database import Base

# ----------------- TABELA DE ASSOCIAÇÃO (Muitos para Muitos) ----------------- #
# Esta tabela física no banco vai armazenar quais produtos pertencem a quais pedidos.
# O nome 'pedido_produto' deve ser exatamente o mesmo usado no secondary do model de Produtos.
pedido_produto = Table(
    "pedido_produto",
    Base.metadata,
    Column("pedido_id", Integer, ForeignKey("pedidos.id", ondelete="CASCADE"), primary_key=True),
    Column("produto_id", Integer, ForeignKey("produtos.id", ondelete="RESTRICT"), primary_key=True)
)


class Pedidos(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    status: Mapped[str] = mapped_column(SQLEnum(
        "pendente", "pago", "enviado", "entregue", "cancelado" 
    ))
    valor_total: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)

    # -------------------- LIGAÇÕES (RELACIONAMENTOS) -------------------- #

    produtos: Mapped[list["Produtos"]] = relationship(
        secondary=pedido_produto,
        back_populates="pedidos"
    )