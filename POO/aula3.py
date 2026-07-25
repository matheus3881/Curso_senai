class Ecommerce:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self._preco = preco
        self.estoque = estoque


    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo")
        self._preco = novo_preco
    
    def aplicar_desconto(self, desconto: float):
        if desconto < 0:
            print("O valor do desconto não pode ser negativo")
            return 
        self.preco = self._preco - desconto
    

    def __str__(self):
        return f"Produto: {self.nome}, preço R$ {self.preco:.2f}"


ecommerce1 = Ecommerce("Iphone 16e", 4000.00, 102)
ecommerce2 = Ecommerce("Samsung S25 FE", 3000.00, 100)

print(ecommerce1)
print(ecommerce2)

valor_com_desconto = ecommerce1.aplicar_desconto(500)
valor_com_desconto = ecommerce2.aplicar_desconto(-300)
















print("="*70)

print(f"valor com desconto: {ecommerce1}")
print(f"valor com desconto: {ecommerce2}")


class Produto:
    def __init__(self, preco, quantidade):
        self.preco = preco 
        self.quantidade = quantidade

    @property   
    def total(self):
        return self.preco * self.quantidade
    

produto1 = Produto(1000, 3)

print(produto1.total)