from fastapi import APIRouter, HTTPException
from models.aluno import AlunoEntrada, AlunoResposta, AlunoPach

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/alunos", status_code=201)
def criar_aluno(aluno: AlunoEntrada):
    novo = aluno.model_dump()
    novo["id"] = max([a["id"] for a in alunos], default=0)=1
    alunos.append(novo)
    return novo



@router.get("/alunos")
def listar_alunos():
    pass

