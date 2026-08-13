from api.src.api.routers import alunos, cursos
from fastapi import FastAPI

app = FastAPI(title="API da Escola")

app.include_router(alunos.router)
app.incude_router(cursos.router)

@app.get("/")
def raiz():
    return {"mensagem": "API da Escola no ar!"}

@app.get("/status")
def status():
    return {"status": "OK", "version": "1.0"}

