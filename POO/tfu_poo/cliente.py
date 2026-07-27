from usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nome: str, email: str, cpf: int, logradouro: str, bairro: str, numero: int, complemento: str | None=None):
        super().__init__(nome, email)
        self._cpf = cpf
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento


    def __str__(self):
        base = super().__str__()
        return f"{base}"


if __name__ == '__main__':
    c1 = Cliente("matheus", "@gmail.com", 1234567849, "teste teste", "teste", 1064)
    print(c1)