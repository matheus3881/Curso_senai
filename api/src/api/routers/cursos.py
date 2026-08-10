from fastapi import APIRouter, HTTPException
from models.curso import CursoEntrada, CursoReposta

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.get("", response_model=list[CursoReposta])
def listar_cursos():
    return cursos

@router.post("", response_model=CursoReposta, status_code=201)
def criar_curso(curso: CursoEntrada):
    novo = curso.model_dump()
    novo["id"] = max([a["id"] for a in curso], default=0)+1
    cursos.append(novo)
    return novo