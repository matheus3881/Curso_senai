def tratarEntrada(entrada: str):
  while True:
    try:
      celsius = float(input(entrada))
    except:
      print("formato númerico inválido")
      continue

    return celsius

celsius = tratarEntrada("Digite a temperatura em graus Celsius: ")
fahrenheit = (celsius * 1.8) + 32

print(f"\n{celsius:.2f} °C equivalem a {fahrenheit:.2f} °F")