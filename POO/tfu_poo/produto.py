
class Produto:
    def __init__(self, id: int, nome: str, preco: float, estoque: int, descricao: str):
        self.id = id
        self.nome = nome
        self._preco = preco
        self.estoque = estoque
        self.descricao = descricao

    def atualizar_estoque(self, nova_quantidade: int):
        """Atualiza a quantidade do produto no estoque"""
        self.estoque = nova_quantidade

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor
        


    def __str__(self):
        """Mostrar informações do produto"""
        return f"produto: {self.nome} - Valor: R$ {self._preco} - Quantidade em estoque: {self.estoque} - Descrição do produto: {self.descricao}"


p1 = Produto(1, "iphone", 3400.90, 15, "Celular da maçã")

print(p1)

p1.atualizar_estoque(nova_quantidade=12)

print(p1)

print(p1.preco)

p1.preco = 300

print(p1.preco)

