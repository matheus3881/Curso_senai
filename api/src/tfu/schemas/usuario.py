from pydantic import BaseModel, Field

# 1. Schema de Entrada (O usuário manda login e senha limpa para se cadastrar)
class UsuarioEntrada(BaseModel):
    login: str = Field(..., description="Login do usuário")
    senha: str = Field(..., min_length=6, description="Senha em texto puro (mínimo 6 caracteres)")

# 2. Schema de Saída (A API devolve apenas ID e Login, NADA de senhas ou hashes)
class UsuarioResposta(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True

# 3. Schema do Token (O formato exato que o FastAPI exige para o login)
class Token(BaseModel):
    access_token: str
    token_type: str