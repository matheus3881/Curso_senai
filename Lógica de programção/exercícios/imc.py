peso = float(input("Seu peso (kg): "))
altura = float(input("Sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")