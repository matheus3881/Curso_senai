from POO.tfu_poo.exceptions.erros import EstoqueInsuficienteError
from POO.tfu_poo.models.pedido import Pedido
from POO.tfu_poo.models.produto import Produto


class PedidoService:
    @staticmethod
    def processar_comprar(pedido: Pedido, produto: Produto, quantidade):
        try:
            pedido.adicionar_item(produto=produto, quantidade=quantidade)

        except EstoqueInsuficienteError as erro:
            return f"Falha: {erro}"