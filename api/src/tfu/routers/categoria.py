from fastapi import APIRouter, Depends, status
from tfu.models.categoria import Categorias
from tfu.database import SessionDep
from tfu.dependencias import Paginacao
from tfu.excecoes import RecursoNaoEncontrado
from tfu.schemas.categoria import (
    CategoriaResposta,
    CategoriaComProdutos,
    CategoriaEntrada
)

router = APIRouter(tags=["Categoria"], prefix="/categoria")

#----------------GET----------------------#

# 1. Listar todas as categorias com paginação
@router.get("", response_model=list[CategoriaResposta])
def listar_categorias(session: SessionDep, pag: Paginacao = Depends()):
    query = session.query(Categorias)
    return query.offset(pag.skip).limit(pag.limit).all()


# 2. Buscar uma categoria por ID (Trazendo a resposta aninhada com a lista de produtos)
@router.get("/{categoria_id}", response_model=CategoriaComProdutos)
def buscar_categoria(categoria_id: int, session: SessionDep):
    categoria = session.get(Categorias, categoria_id)
    if categoria is None:
        raise RecursoNaoEncontrado("Categoria")
        
    return categoria


#----------------POST----------------------#

# 3. Criar uma nova categoria
@router.post("", status_code=status.HTTP_201_CREATED, response_model=CategoriaResposta)
def criar_categoria(dados: CategoriaEntrada, session: SessionDep):
    categoria = Categorias(**dados.model_dump())
    
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


#----------------PUT----------------------#

# 4. Atualizar totalmente uma categoria
@router.put("/{categoria_id}", response_model=CategoriaResposta)
def atualizar_categoria(categoria_id: int, dados: CategoriaEntrada, session: SessionDep):
    categoria = session.get(Categorias, categoria_id)
    if categoria is None:
        raise RecursoNaoEncontrado("Categoria")
        
    categoria.nome = dados.nome
    
    session.commit()
    session.refresh(categoria)
    return categoria


#----------------DELETE-------------------#

# 5. Remover uma categoria
@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_categoria(categoria_id: int, session: SessionDep):
    categoria = session.get(Categorias, categoria_id)
    if categoria is None:
        raise RecursoNaoEncontrado("Categoria")
        
    session.delete(categoria)
    session.commit()