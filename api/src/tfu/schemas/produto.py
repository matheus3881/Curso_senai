from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

# ----------------- SCHEMA AUXILIAR ----------------- #

class CategoriaMinima(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True




class ProdutoEntrada(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="Nome do produto")
    preco: Decimal = Field(..., gt=0, description="Preço do produto (maior que zero)")
    estoque: int = Field(..., ge=0, description="Quantidade em estoque (não pode ser negativa)")
    descricao: Optional[str] = Field(None, description="Descrição opcional do produto")


class ProdutoPatch(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    preco: Optional[Decimal] = Field(None, gt=0)
    estoque: Optional[int] = Field(None, ge=0)
    descricao: Optional[str] = None


class ProdutosEmLote(BaseModel):
    produtos: list[ProdutoEntrada] = Field(..., description="Lista de produtos para criação em lote")


# ----------------- SCHEMAS DE SAÍDA (OUTPUT) ----------------- #

class ProdutoResposta(BaseModel):
    id: int
    nome: str
    preco: Decimal
    estoque: int
    descricao: Optional[str]
    categoria_id: int  # Retorna a chave estrangeira direta do banco

    class Config:
        from_attributes = True  # Permite mapear os objetos do SQLAlchemy 2.0 automaticamente


class ProdutoComCategoria(ProdutoResposta):
    categoria: CategoriaMinima  # Traz os detalhes da categoria aninhados 

    class Config:
        from_attributes = True