from sqlalchemy.orm import Mapped, mapped_column
from databases import Base

class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primaty_key=True)
    nome: Mapped[str]
    carga_horaria: Mapped[int]