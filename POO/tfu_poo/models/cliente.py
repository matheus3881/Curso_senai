from models.usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nome: str, email: str, cpf: int, logradouro: str, bairro: str, numero: int, complemento: str | None=None):
        super().__init__(nome, email)
        self.cpf = cpf
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)


    def __str__(self):
        base = super().__str__()
        return f"[CLIENTE] {base} - CPF: {self.cpf}"