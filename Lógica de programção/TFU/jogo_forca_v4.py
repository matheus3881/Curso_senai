import random


def imprime_mensagem_abertura():
    print("*" * 35)
    print("***Bem vindo ao jogo da Forca!***")
    print("*" * 35)

def carrega_palavra_secreta():
    palavras = {
        "frutas": ["maçã", "banana"],
        "paises": ["brasil", "frança"],
        "animais": ["cachorro", "gato"]
    }
    categoria, valor = random.choice(list(palavras.items()))
    palavra_secreta = random.choice(valor)
    
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("qual letra? ")
    chute = chute.strip().lower()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            letras_acertadas[index] = letra

    

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\\\  ")
    print("\\|   XXXX     XXXX   |/    ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)
    letras_tentadas = []


    print(letras_acertadas)
    while True:
        
        chute = pede_chute()
        if len(chute) !=1 or not chute.isalpha():
            print("Digite uma letra válida")
            continue

        if chute in letras_tentadas:
            print("Você já tentou essa letra! tente outra.")
            continue

        print('------------------------------------')
        letras_tentadas.append(chute)
        print(f"LETRAS TENTADAS: {letras_tentadas}")

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            pontuacao = pontuacao + 10
            letras_faltando = letras_acertadas.count('_')
            desenha_forca(erros)
        else:
                erros += 1
                print(letras_acertadas)
                print("Ainda faltam acertar {}".format(letras_faltando))
                print("Você ainda tem {} tentativas".format(6-erros))
                desenha_forca(erros)
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


        if(acertou):
            imprime_mensagem_vencedor() 
            break

            
        if(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)
            break




if(__name__ == '__main__'):
    jogando = True
    while jogando:
        jogar()
        jogando = input("Deseja continuar? (S/N) ").strip().lower() == "s"
    
    print(f"sua pontuação é: {pontuacao}")
    print('Fim do jogo')