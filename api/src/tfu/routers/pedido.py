from fastapi import APIRouter, Depends, status
from tfu.models.pedido import Pedidos
from tfu.models.produto import Produtos
from tfu.database import SessionDep
from tfu.dependencias import Paginacao
from tfu.excecoes import RecursoNaoEncontrado
from tfu.schemas.pedido import (
    PedidoResposta,
    PedidoComProdutos,
    PedidoEntrada
)

router = APIRouter(tags=["Pedido"], prefix="/pedido")

#----------------GET----------------------#

@router.get("", response_model=list[PedidoResposta])
def listar_pedidos(session: SessionDep, pag: Paginacao = Depends()):
    query = session.query(Pedidos)
    return query.offset(pag.skip).limit(pag.limit).all()


@router.get("/{pedido_id}", response_model=PedidoComProdutos)
def buscar_pedido(pedido_id: int, session: SessionDep):
    pedido = session.get(Pedidos, pedido_id)
    if pedido is None:
        raise RecursoNaoEncontrado("Pedido")
        
    return pedido


#----------------POST----------------------#

@router.post("", status_code=status.HTTP_201_CREATED, response_model=PedidoComProdutos)
def criar_pedido(dados: PedidoEntrada, session: SessionDep):
    dados_pedido = dados.model_dump(exclude={"produtos_ids"})
    novo_pedido = Pedidos(**dados_pedido)
    
    for produto_id in dados.produtos_ids:
        produto = session.get(Produtos, produto_id)
        if produto is None:
            raise RecursoNaoEncontrado(f"Produto com ID {produto_id}")
            
        novo_pedido.produtos.append(produto)
    
    session.add(novo_pedido)
    session.commit()
    session.refresh(novo_pedido)
    return novo_pedido


#----------------DELETE-------------------#

@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_pedido(pedido_id: int, session: SessionDep):
    pedido = session.get(Pedidos, pedido_id)
    if pedido is None:
        raise RecursoNaoEncontrado("Pedido")
        
    session.delete(pedido)
    session.commit()