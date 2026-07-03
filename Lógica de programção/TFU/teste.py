import random

forca_ascii = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


categorias = {
    "frutas": ["banana", "maçã", "uva", "laranja", "pera"],
    "animais": ["gato", "cachorro", "elefante", "leão", "tigre"],
    "países": ["brasil", "argentina", "chile", "peru", "méxico"]
}

def jogo_da_forca():
    print("======= Jogo da Forca =======")
    pontuacao = 0
    jogar_novamente = "s"

    while jogar_novamente == "s":
        # Escolher categoria
        print("\nCategorias disponíveis:")
        for cat in categorias.keys():
            print("-", cat)
        escolha = input("Escolha uma categoria: ").lower()

        if escolha not in categorias:
            print("Categoria inválida. Escolha novamente.")
            continue

        palavra = random.choice(categorias[escolha])
        letras_descobertas = ["_"] * len(palavra)
        tentativas = 6
        letras_erradas = []

        while tentativas > 0 and "_" in letras_descobertas:
            print(forca_ascii[6 - tentativas])
            print("Palavra:", " ".join(letras_descobertas))
            print("Tentativas restantes:", tentativas)
            print("Letras erradas:", " ".join(letras_erradas))
            print("Pontuação atual:", pontuacao)

            letra = input("Digite uma letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas uma letra válida.")
                continue

            if letra in palavra:
                for i, l in enumerate(palavra):
                    if l == letra:
                        letras_descobertas[i] = letra
                print("Boa! Você acertou uma letra.")
                pontuacao += 10  # cada acerto vale 10 pontos
            else:
                if letra not in letras_erradas:
                    letras_erradas.append(letra)
                    tentativas -= 1
                    print("Ops! Essa letra não está na palavra.")
                else:
                    print("Você já tentou essa letra antes.")

        if "_" not in letras_descobertas:
            print("\nParabéns! Você venceu! 🎉")
            print("A palavra era:", palavra)
            pontuacao += 50  # bônus por vencer
        else:
            print("\nFim de jogo! Você perdeu. 😢")
            print("A palavra era:", palavra)

        print("Pontuação final desta rodada:", pontuacao)
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()

    print("\nObrigado por jogar! Sua pontuação total foi:", pontuacao)


if __name__ == "__main__":
    jogo_da_forca()