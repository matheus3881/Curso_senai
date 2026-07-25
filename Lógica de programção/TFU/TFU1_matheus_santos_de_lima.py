import random


def imprime_mensagem_abertura():
    print("*" * 35)
    print("***Bem vindo ao jogo da Forca!***")
    print("*" * 35)

# Sorteia a palavra e a categoria
def carrega_palavra_secreta():
    palavras = {
        "frutas": ["maçã", "banana", "laranja", "uva", "morango"], 
        "paises": ["brasil", "frança", "japão", "canadá", "egito"],
        "animais": ["cachorro", "gato", "elefante", "leão", "girafa"]
    }
    categoria, valor = random.choice(list(palavras.items()))
    palavra_secreta = random.choice(valor)
    
    return palavra_secreta, categoria

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


def jogar(pontuacao_atual):
    imprime_mensagem_abertura()

    palavra_secreta, categoria_sorteada = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)
    letras_tentadas = []

    print(f"\nDICA: A palavra secreta pertence à categoria '{categoria_sorteada.upper()}'! ")
    print(f"ATENÇÃO: Cada letra acertada vale 10 pts!")
    print()
    print(letras_acertadas)

    while True:
        
        
        chute = pede_chute()
        if len(chute) !=1 or not chute.isalpha():
            print("Digite uma letra válida")
            continue

        # Evita que o jogador perca vida com letra repetida
        if chute in letras_tentadas:
            print("Você já tentou essa letra! tente outra.")
            continue

        print()
        print('------------------------------------')
        letras_tentadas.append(chute)
        print(f"LETRAS TENTADAS: {letras_tentadas}")
        print()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = letras_acertadas.count('_')
            desenha_forca(erros)
        else:
            erros += 1
            # print(letras_acertadas)
            print("Ainda faltam acertar {}".format(letras_faltando))
            print("Você ainda tem {} tentativas".format(6-erros))
            desenha_forca(erros)
            print('------------------------------------')
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


        if(acertou):
            imprime_mensagem_vencedor() 

            pontos_base = len(palavra_secreta) * 10
            print(f"\nVocê fez {pontos_base} pontos nesta rodada!")
            
            nova_pontuacao = pontuacao_atual + pontos_base
            print(f"🏆 PLACAR TOTAL: {nova_pontuacao} pontos 🏆\n")

            return nova_pontuacao

            
        if(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)
            print(f"PLACAR TOTAL: {pontuacao_atual} pontos \n")
            return pontuacao_atual
            


if(__name__ == '__main__'):
    pontuacao_total = 0
    jogando = True
    while jogando:

        pontuacao_total = jogar(pontuacao_total)

        escolha = input("Deseja continuar? (S/N) ").strip().lower() == "s"
        if(not escolha):
            break
    
    print('Fim do jogo')