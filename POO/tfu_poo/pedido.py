class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_total = produto.preco * quantidade

    def mostrar_item(self):
         return f"{self.quantidade}x {self.produto.nome} - R${self.preco_total:.2f}"

class Pedido:
    def __init__(self, id: int, data: str, valorTotal: float):
        self.id = id
        self.data = data
        self.valorTotal = valorTotal
        self.status = "PENDENTE" # PENDENTE, PAGO, ENVIADO, ENTREGUE
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto.preco(quantidade):
            item = ItemPedido(produto, quantidade)
            self.itens.append(item)
            self.valorTotal += item.preco_total
            return True
        return False
    
    def mostrar_pedido(self):
        info = f"pedido #{self.id} - Status: {self.status}\n"
        info += f"Cliente: {self.cliente.nome}\n"
        info += f"Itens:\n"

        for item in self.itens:
            info += f" - {item.mostrar_item()}\n"

        info += f"Total: R$ {self.valorTotal:.2f}"
        return info
    
    def mudar_status(self, novo_status):
        self.status = novo_status
        print(f"Status do pedido #{self.id} alteradi para: {novo_status}")
        





