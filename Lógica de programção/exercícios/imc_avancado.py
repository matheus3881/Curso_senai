def lerPeso(mensagem):
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            peso = float(entrada)
        except ValueError:
            print("Erro: digite um número válido.")
            continue

        if peso <= 0:
            print("Erro: o peso deve ser maior que zero.")
            continue

        return peso

def lerAltura(mensagem):
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            altura = float(entrada)
        except ValueError:
            print("Erro: digite um número válido.")
            continue

        if altura <= 0:
            print("Erro: a altura deve ser maior que zero.")
            continue

        if altura > 2.5:
              altura = altura / 100

        return altura

peso = lerPeso("Seu peso (kg): ")
altura = lerAltura("Sua altura (m ou cm): ")

imc = peso / (altura ** 2)

print("---------------------------------")
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade grau I.")
elif imc < 40:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III.")