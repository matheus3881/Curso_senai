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

# @app.get("/")
# def read_root():
#     return {"Hello": "matheus"}

# @app.get("/status")
# def status():
#     return{"status": "ok", 
#            "version": "q.0" }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}