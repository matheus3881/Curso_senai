class Pedido:
    def __init__(self, id_Pedido, cliente):
        self.id_Pedido = id_Pedido
        self.cliente = cliente
        self.itens = []  # Esta lista vai guardar os objetos do tipo Produto

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        # Soma o preço de cada objeto Produto armazenado na lista itens
        return sum(produto.preco for produto in self.itens)


class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco


# 1. Criando as instâncias de Produto com os dados necessários
notebook = Produto(101, "Notebook", 4000.00)
mouse = Produto(102, "Mouse", 150.00)

# 2. Criando o Pedido
pedido1 = Pedido(1, "matheus")

# 3. Fazendo a composição (inserindo os produtos dentro do pedido)
pedido1.adicionar_item(notebook)
pedido1.adicionar_item(mouse)

# 4. Mostrando o resultado
print(f"Pedido de {pedido1.cliente} tem {len(pedido1.itens)} itens.")
print(f"Valor Total: R$ {pedido1.calcular_total():.2f}")
