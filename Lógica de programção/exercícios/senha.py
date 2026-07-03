senha = str(input('senha: '))

if len(senha) == 8 and '@' in senha:
    print("ok")
else:
    print("Errado")