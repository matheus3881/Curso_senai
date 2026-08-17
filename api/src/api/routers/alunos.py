from fastapi import APIRouter, HTTPException
from aluno import AlunoEntrada, AlunoResposta, AlunoPatch
from api.src.api.database import SessionLocal
from models.aluno import Aluno


router = APIRouter(prefix="/alunos", tags=["Alunos"])

alunos = [
    {"id": 1, "nome": "Ana Souza","idade": 28, "ativo": True},
    {"id": 2, "nome": "Bruno Lima","idade": 22, "ativo": True},
    {"id": 3, "nome": "Carla Dias","idade": 30, "ativo": False},
]


# ---------------------- GET ------------------------- #

@router.get("", response_model=list[AlunoResposta])
def listar_alunos(ativo: bool | None = None, limite:int = 10):
    with SessionLocal() as session:
        query = session.query(Aluno)
        if ativo is not None:
            query = query.filter(Aluno.ativo == ativo)
        return session.query(Aluno).all()


@router.get("/{aluno_id}", response_model=AlunoResposta)
def buscar_aluno(aluno_id: int):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return aluno

# ---------------------------- POST ------------------------ #
@router.post("", response_model=AlunoResposta, status_code=201)
def criar_aluno(dados: AlunoEntrada):
    with SessionLocal() as session:
        aluno = Aluno(**dados.model_dump())
        session.add(aluno)
        session.commit()
        return aluno

# ----------------------------- PUT -------------------------- #
@router.put("/{aluno_id}", response_model=AlunoResposta)
def atualizar_aluno(aluno_id: int, dados: AlunoEntrada):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        aluno.nome = dados.nome
        aluno.idade = dados.idade
        aluno.ativo = dados.ativo
        session.commit()
        return aluno


# ---------------------------- PATCH -------------------------- #
@router.patch("/{aluno_id}", response_model=AlunoEntrada)
def alterar_aluno(aluno_id: int, dados: AlunoPatch):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        mudancas = dados.model_dump(exclude_unset=True)
        for campo, valor in mudancas.items():
            setattr(aluno, campo, valor)
        session.commit()
        return aluno

# ---------------------------- DELETE -------------------------- #
@router.delete("/{aluno_id}")
def remover_aluno(aluno_id: int):
    with SessionLocal() as session:
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        session.delete(aluno)
        session.commit()
        return{"mensagem": "Aluno removido com sucesso!"}