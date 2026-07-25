class Ecommerce:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def aplicar_desconto(self, valor):
        self.preco = self.preco - valor

    
    def __str__(self):
        return f"Produto: {self.nome}, preço R$ {self.preco:.2f}"


ecommerce1 = Ecommerce("Iphone 16e", 4000.00, 102)
ecommerce2 = Ecommerce("Samsung S25 FE", 3000.00, 100)

print(ecommerce1)
print(ecommerce2)

valor_com_desconto = ecommerce1.aplicar_desconto(500)
valor_com_desconto = ecommerce2.aplicar_desconto(300)

print("="*70)

print(f"valor com desconto: {ecommerce1}")
print(f"valor com desconto: {ecommerce2}")


