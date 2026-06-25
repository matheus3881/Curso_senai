def tratarPreco(entrada: str):
  while True:
    try:
      preco_unitario = float(input(entrada))
    except:
      print("formato númerico inválido")
      continue

    return preco_unitario

def tratarQuantidade(entrada: str):
  while True:
    try:
      quantidade_comprada = int(input(entrada))
    except:
      print("formato númerico inválido")
      continue

    return quantidade_comprada



preco_unitario = tratarPreco("Informe o preço unitário do produto: R$ ")
quantidade_comprada = tratarQuantidade("Informe a quantidade comprada: ")

valor_total = quantidade_comprada * preco_unitario
print(f"total a pagar R$ {valor_total:.2f}")
print(type(valor_total))