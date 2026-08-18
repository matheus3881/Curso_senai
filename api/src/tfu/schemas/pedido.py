from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from tfu.schemas.produto import ProdutoResposta

# ----------------- SCHEMAS DE ENTRADA (INPUT) ----------------- #

class PedidoEntrada(BaseModel):
    produtos_ids: list[int] = Field(..., description="Lista de IDs de produtos que vão compor o pedido")
    status: Optional[str] = Field("pendente", description="Status do pedido")
    valor_total: Decimal = Field(..., gt=0, description="Valor total da compra")


# ----------------- SCHEMAS DE SAÍDA (OUTPUT) ----------------- #

class PedidoResposta(BaseModel):
    id: int
    data: datetime
    status: str
    valor_total: Decimal

    class Config:
        from_attributes = True


class PedidoComProdutos(PedidoResposta):
    produtos: list[ProdutoResposta] = [] 

    class Config:
        from_attributes = True