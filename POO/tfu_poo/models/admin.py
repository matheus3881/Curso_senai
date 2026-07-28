from POO.tfu_poo.models.usuario import Usuario

class Admin(Usuario):
    def __str__(self):
        return super().__str__()
    
if __name__ == '__main__':

    a1 = Admin("adm", "adm@gmail.com")
    print(a1)
