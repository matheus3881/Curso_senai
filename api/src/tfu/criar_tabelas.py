from tfu.database import engine, Base
# CRUCIAL: Importar todos os modelos para o SQLAlchemy "conhecer" as tabelas
from tfu.models.categoria import Categorias
from tfu.models.produto import Produtos
from tfu.models.pedido import Pedidos
from tfu.models.usuario import Usuarios

print("Criando tabelas do E-commerce no SQLite...")
# Cria fisicamente as tabelas que foram importadas acima
Base.metadata.create_all(bind=engine)
print("Tabelas geradas com sucesso dentro da pasta correta!")