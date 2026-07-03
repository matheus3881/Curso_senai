idade = int(input("Sua idade: "))
tem_ingresso = input("Tem ingresso? (s/n): ") == "s"
eh_vip = input("É VIP? (s/n): ") == "s"

maior_18 = idade >= 18
pode_entrar = maior_18 and (tem_ingresso or eh_vip)

print(f"Maior de 18? {maior_18}")
print(f"Pode entrar? {pode_entrar}")