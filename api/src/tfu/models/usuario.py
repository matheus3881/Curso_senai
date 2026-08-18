from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from tfu.database import Base

class Usuarios(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    # A senha real NUNCA fica no banco, apenas o hash gerado a partir dela
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)