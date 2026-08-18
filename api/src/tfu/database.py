from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from pathlib import Path

# Descobre automaticamente o caminho da pasta onde este arquivo 'database.py' está guardado
DIRETORIO_ATUAL = Path(__file__).parent.resolve()

# Força o banco a ser criado exatamente dentro da pasta atual do projeto
URL_BANCO = f"sqlite:///{DIRETORIO_ATUAL}/ecommerce.db"

# Cria o motor do banco de dados
engine = create_engine(
    URL_BANCO, 
    connect_args={"check_same_thread": False}
)

# CORREÇÃO: Inicializa o sessionmaker corretamente com os parênteses e parâmetros
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependência do Banco de Dados para os Routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apelido utilizado nas rotas
SessionDep = Annotated[Session, Depends(get_db)]