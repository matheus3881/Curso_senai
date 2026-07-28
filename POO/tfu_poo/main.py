from models.admin import Admin
from models.cliente import Cliente
from models.pedido import Pedido
from models.produto import Produto
from services.pedido_service import PedidoService


def main() -> None:
    # 1. Criação dos objetos com seus respectivos atributos obrigatórios
    matheus = Cliente(nome="Matheus", email="matheus@gmail.com", cpf=12345678900, logradouro="Rua das Flores", bairro="Centro", numero=1064)
    adm = Admin(nome="Chefe", email="admin@ecommerce.com")
    
    iphone = Produto(id=1, nome="iPhone 15", preco=4500.00, estoque=10, descricao="Celular da maçã")
    fone = Produto(id=2, nome="AirPods Pro", preco=1500.00, estoque=2, descricao="Fone sem fio com cancelamento de ruído")
    
    pedido1 = Pedido(id=1001, data="28/07/2026", cliente=matheus)

    # 2. Testando o Polimorfismo e as classes abstratas
    print("--- USUÁRIOS DO SISTEMA ---")
    print(adm)
    print(matheus)
    print("-" * 40)

    # 3. Adicionando o pedido na lista de histórico do cliente
    matheus.adicionar_pedido(pedido1)

    # 4. Orquestrando as compras via Service (Controller)
    print("--- PROCESSANDO COMPRAS ---")
    
    # Compra com sucesso (reduz estoque do iphone para 8)
    print(PedidoService.processar_compra(pedido1, iphone, 2))
    
    # Compra com sucesso (zera o estoque do fone)
    print(PedidoService.processar_compra(pedido1, fone, 2))
    
    # Compra que DEVE FALHAR e disparar o EstoqueInsuficienteError
    print(PedidoService.processar_compra(pedido1, fone, 1))
    
    print("-" * 40)

    # 5. Exibindo o uso do método especial __str__ e os cálculos finais
    print("--- NOTA FISCAL ---")
    print(pedido1)
    print("-" * 40)
    
    # 6. Atualização de status
    print("--- ATUALIZAÇÃO ---")
    print(pedido1.mudar_status("PAGO"))


if __name__ == "__main__":
    main()