from pydantic import BaseModel, Field
from typing import Optional
from tfu.schemas.produto import ProdutoResposta  # Importa o schema de saída do produto

# ----------------- SCHEMAS DE ENTRADA (INPUT) ----------------- #

# Dados que chegam do cliente na criação (POST) ou atualização total (PUT)
class CategoriaEntrada(BaseModel):
    nome: str = Field(..., min_length=2, max_length=20, description="Nome da categoria")
    descricao: Optional[str] = Field(None, max_length=255, description="Descrição opcional da categoria")


# Dados para atualização parcial (PATCH) - tudo se torna opcional
class CategoriaPatch(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=20)
    descricao: Optional[str] = Field(None, max_length=255)


# ----------------- SCHEMAS DE SAÍDA (OUTPUT) ----------------- #

# Resposta simples (Usada na listagem geral via GET /categoria)
class CategoriaResposta(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]

    class Config:
        from_attributes = True  # Permite que o Pydantic leia direto do model do SQLAlchemy


# Resposta Aninhada Completa (Exigência do TFU para o GET /categoria/{id})
# Retorna os dados da categoria e automaticamente a lista de produtos vinculados a ela
class CategoriaComProdutos(CategoriaResposta):
    produtos: list[ProdutoResposta] = []  # Lista os produtos usando o schema de resposta deles

    class Config:
        from_attributes = True