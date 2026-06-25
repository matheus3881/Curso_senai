preco_unitario = float(input("Informe o preço unitário do produto: R$ "))
quantidade_comprada = int(input("Informe a quantidade comprada: "))

valor_total = quantidade_comprada * preco_unitario

print(f"total a pagar R$ {valor_total:.2f}")
print(type(valor_total))