from fastapi import APIRouter, Depends, status
from tfu.models.produto import Produtos
from tfu.models.categoria import Categorias # Adicionado para o relacionamento
from tfu.database import SessionDep
from tfu.dependencias import Paginacao
from tfu.excecoes import RecursoNaoEncontrado
from tfu.schemas.produto import (
    ProdutoResposta, 
    ProdutoComCategoria, 
    ProdutoEntrada, 
    ProdutoPatch, 
    ProdutosEmLote
)

router = APIRouter(tags=["Produto"], prefix="/produto")

#----------------GET----------------------#
@router.get("", response_model=list[ProdutoResposta])
def listar_produtos(session: SessionDep, pag: Paginacao = Depends(), disponivel: bool | None = None):
    query = session.query(Produtos)
    
    # Filtro opcional
    if disponivel is not None:
        query = query.filter(Produtos.disponivel == disponivel)
        
    # Correção: aplicando o limite e offset em cima da query filtrada
    return query.offset(pag.skip).limit(pag.limit).all()

@router.get("/{produto_id}", response_model=ProdutoComCategoria)
def buscar_produto(produto_id: int, session: SessionDep):
    produto = session.get(Produtos, produto_id)
    if produto is None:
        raise RecursoNaoEncontrado("Produto")
        
    return produto


#----------------POST----------------------#
# Rota para criar um produto vinculado a uma categoria
@router.post("/{categoria_id}", status_code=status.HTTP_201_CREATED, response_model=ProdutoComCategoria)
def criar_produto(categoria_id: int, dados: ProdutoEntrada, session: SessionDep):
    # 1. Verifica se a categoria existe
    categoria = session.get(Categorias, categoria_id)
    if categoria is None:
        raise RecursoNaoEncontrado("Categoria")
        
    # 2. Cria o produto e faz o vínculo
    produto = Produtos(**dados.model_dump())
    produto.categoria = categoria 
    
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto

# Criação em lote (Requisito Bônus)
@router.post("/lote/{categoria_id}", status_code=status.HTTP_201_CREATED, response_model=list[ProdutoComCategoria])
def criar_produtos_em_lote(categoria_id: int, dados: ProdutosEmLote, session: SessionDep):
    categoria = session.get(Categorias, categoria_id)
    if categoria is None:
        raise RecursoNaoEncontrado("Categoria")
        
    novos_produtos = []
    for item in dados.produtos:
        produto = Produtos(**item.model_dump())
        produto.categoria = categoria
        novos_produtos.append(produto)
        
    session.add_all(novos_produtos)
    session.commit()
    return novos_produtos


#----------------PUT----------------------#
@router.put("/{produto_id}", response_model=ProdutoResposta)
def atualizar_produto(produto_id: int, dados: ProdutoEntrada, session: SessionDep):
    produto = session.get(Produtos, produto_id)
    if produto is None:
        raise RecursoNaoEncontrado("Produto")
        
    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.disponivel = dados.disponivel
    
    session.commit()
    session.refresh(produto)
    return produto


#----------------PATCH----------------------#
@router.patch("/{produto_id}", response_model=ProdutoResposta)
def alterar_produto(produto_id: int, dados: ProdutoPatch, session: SessionDep):
    produto = session.get(Produtos, produto_id)
    if produto is None:
        raise RecursoNaoEncontrado("Produto")
        
    mudancas = dados.model_dump(exclude_unset=True)
    for campo, valor in mudancas.items():
        setattr(produto, campo, valor)
        
    session.commit()
    session.refresh(produto)
    return produto


#----------------DELETE-------------------#
@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_produto(produto_id: int, session: SessionDep):
    produto = session.get(Produtos, produto_id)
    if produto is None:
        raise RecursoNaoEncontrado("Produto")
        
    session.delete(produto)
    session.commit()