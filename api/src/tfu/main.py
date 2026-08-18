from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from tfu.routers import autenticacao, produto, categoria, pedido
from tfu.excecoes import RecursoNaoEncontrado

app = FastAPI(
    title="API E-commerce Avançado SENAI",
    description="Módulo 5 - Desenvolvimento de API RESTful",
    version="1.0.0"
)

# Centralização do 404 via Exception Handler (Critério 4.5 do TFU)
@app.exception_handler(RecursoNaoEncontrado)
def handler_recurso_nao_encontrado(request: Request, exc: RecursoNaoEncontrado):
    return JSONResponse(
        status_code=404,
        content={"detail": exc.mensagem}
    )

@app.exception_handler(IntegrityError)
def handler_erro_integridade(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=409,  # 409 significa "Conflict" (Conflito de dados)
        content={"detail": "Operação negada: Já existe um registro com estes dados únicos no sistema ou há um conflito de relacionamento."}
    )

# Acoplando as rotas
app.include_router(autenticacao.router)
app.include_router(categoria.router)
app.include_router(produto.router)
app.include_router(pedido.router)

@app.get("/")
def home():
    return {"status": "Online", "docs": "/docs"}