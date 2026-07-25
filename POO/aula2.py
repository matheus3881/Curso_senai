class Aluno:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def atualizar_email(self, novo_email):
        self.email = novo_email

    def __str__(self):
        return f"Aluno: {self.nome} - e-mail: {self.email}"

    
aluno1 = Aluno("matheus", "102", "matheus@teste.com")

aluno1.atualizar_email("matheus@gmail.com")

print(aluno1)