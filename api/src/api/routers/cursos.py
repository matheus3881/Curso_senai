from fastapi import APIRouter, HTTPException
from models.curso import CursoEntrada, CursoReposta

router = APIRouter(prefix="/cursos", tags=["Cursos"])

cursos = [
    {"id": 1, "nome": "Python Back-End", "carga_horaria": 180},
    {"id": 2, "nome": "Desenvolvimento Front-End", "carga_horaria": 160},
    {"id": 3, "nome": "Banco de Dados com MySQL", "carga_horaria": 32},
    {"id": 4, "nome": "DevOps e Cloud", "carga_horaria": 120},
    {"id": 5, "nome": "Análise de Dados", "carga_horaria": 90},
]

@router.get("", response_model=list[CursoReposta])
def listar_cursos():
    return cursos

@router.post("", response_model=CursoReposta, status_code=201)
def criar_curso(curso: CursoEntrada):
    novo = curso.model_dump()
    novo["id"] = max([c["id"] for c in curso], default=0)+1
    cursos.append(novo)
    return novo