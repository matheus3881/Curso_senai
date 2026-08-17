

from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum

from tfu.database import Base


class Pedido(Base):

    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    status: Mapped[str] = mapped_column(SQLEnum(
        "pendente", "pago", "enviado", "entregue", "cancelado" 
    ))
    valor_total: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)