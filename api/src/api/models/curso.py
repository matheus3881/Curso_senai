from pydantic import BaseModel, Field

class CursoEntrada(BaseModel):
    nome: str = Field(min_length=3)
    carga_hoaria: int = Field(gt=0)


class CursoReposta(BaseModel):
    id: int
    nome: str
    carga_horaria: int