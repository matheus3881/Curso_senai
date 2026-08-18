class RecursoNaoEncontrado(Exception):
    def __init__(self, nome_recurso: str):
        self.nome_recurso = nome_recurso
        self.mensagem = f"{nome_recurso} não encontrado(a)."
        super().__init__(self.mensagem)