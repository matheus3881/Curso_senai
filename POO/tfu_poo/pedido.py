class Pedido:
    def __init__(self, id: int, data: str, status: str, valorTotal: float):
        self.id = id
        self.data = data
        self.status = status
        self.valorTotal = valorTotal


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_total = produto.preco * quantidade


