from database import SessionLocal
from models.aluno import Aluno
from models.curso import Curso

session = SessionLocal()

novo_aluno = Aluno(nome="Matheus Santos", idade=25)
session.add(novo_aluno)
session.commit()

novo_curso = Curso(nome="HTML - Básico", carga_horaria=5)
session.add(novo_curso)
session.commit()

print(novo_aluno.id)
print(novo_curso.id)
session.close()