usuario = input("Digite seu login: ")
senha = int(input("Digite sua senha: "))

senha_correta = 1234

if (usuario.lower() == "admin" and senha == senha_correta):
    print(f"Bem-vindo administrador {usuario}")   
else:
    print(f"Bem-vindo usuário {usuario}")