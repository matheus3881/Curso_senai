from exceptions.erros import EstoqueInsuficienteError
from models.pedido import Pedido
from models.produto import Produto


class PedidoService:
    @staticmethod
    def processar_compra(pedido: Pedido, produto: Produto, quantidade: int):
        try:
            pedido.adicionar_item(produto=produto, quantidade=quantidade)
            return f"Sucesso: {quantidade}x {produto.nome} adicionado ao carrinho!"
        except EstoqueInsuficienteError as erro:
            return f"Falha: {produto.nome} - {erro}"