
class Produto:
    def __init__(self, id: int, nome: str, preco: float, estoque: int, descricao: str):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao

    def atualizarEstoque(self, nova_quantidade: int):
        """Atualiza a quantidade do produto no estoque"""
        self.estoque = nova_quantidade
        


    def __str__(self):
        """Mostrar informações do produto"""
        return f"produto: {self.nome} - Valor: R$ {self.preco} - Quantidade em estoque: {self.estoque} - Descrição do produto: {self.descricao}"


p1 = Produto(1, "iphone", 3400.90, 15, "Celular da maçã")

print(p1)

p1.atualizarEstoque(nova_quantidade=12)

print(p1)