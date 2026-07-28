from POO.tfu_poo.exceptions.erros import EstoqueInsuficienteError
from POO.tfu_poo.models.produto import Produto
from POO.tfu_poo.models.cliente import Cliente


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_total = produto.preco * quantidade

    def __str__(self):
         return f"{self.quantidade}x {self.produto.nome} - R${self.preco_total:.2f}"

class Pedido:
    def __init__(self, id: int, data: str, cliente: Cliente):
        self.id = id
        self.data = data
        self.valor_total = 0.0
        self.status = "PENDENTE" # PENDENTE, PAGO, ENVIADO, ENTREGUE
        self.itens = []
        self.cliente = cliente

    def adicionar_item(self, produto, quantidade):
        if produto.estoque >= quantidade:
            item = ItemPedido(produto, quantidade)
            self.itens.append(item)
            produto.atualizar_estoque(produto.estoque - quantidade)
            self.valor_total += item.preco_total
            return True
        raise EstoqueInsuficienteError("Estoque insuficiente")
    
    def __str__(self):
        info = f"pedido #{self.id} - Status: {self.status}\n"
        info += f"Cliente: {self.cliente.nome}\n"
        info += f"Itens:\n"

        for item in self.itens:
            info += f" - {str(item)}\n"

        info += f"Total: R$ {self.valor_total:.2f}"
        return info
    
    def mudar_status(self, novo_status):
        self.status = novo_status
        print(f"Status do pedido #{self.id} alteradi para: {novo_status}")
        