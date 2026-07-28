from models.usuario import Usuario

class Admin(Usuario):
    def __str__(self):
        return f"{super().__str__()} - ADMIN"  