from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    @abstractmethod
    def __str__(self):
        return f"Nome: {self.nome} - E-mail: {self.email}"