nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
frequencia = float(input("Digite a frequência do aluno (apenas números, ex: 75.5): "))

media = (nota1 + nota2) / 2

if media >= 7 and frequencia >= 75:
    print(f"Aprovado!! com média: {media:.1f} e frequência: {frequencia}%")
else:
    print(f"Tente ano que vem novamente")