from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from tfu.database import SessionDep
from tfu.models.usuario import Usuarios
from tfu.schemas.usuario import UsuarioEntrada, UsuarioResposta, Token
from tfu.utils.seguranca import gerar_senha_hash, verificar_senha, criar_token_acesso

router = APIRouter(tags=["Autenticação"])

# 1. Endpoint de Registro (/registrar)
# Recebe login/senha e devolve apenas os dados públicos do usuário (protegendo a senha)
@router.post("/registrar", status_code=status.HTTP_201_CREATED, response_model=UsuarioResposta)
def registrar_usuario(dados: UsuarioEntrada, session: SessionDep):
    print(f"👉 DEBUG - Senha que a API recebeu: '{dados.senha}'")
    print(f"👉 DEBUG - Tamanho dessa senha: {len(dados.senha)} caracteres")
    # Verifica se o login já existe no sistema
    usuario_existente = session.query(Usuarios).filter(Usuarios.login == dados.login).first()
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Este login já está sendo utilizado."
        )
        
    # Criptografa a senha antes de mandar para o banco (Critério 4.7)
    senha_criptografada = gerar_senha_hash(dados.senha)
    
    novo_usuario = Usuarios(
        login=dados.login,
        senha_hash=senha_criptografada
    )
    
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)
    return novo_usuario


# 2. Endpoint de Login (/token) que devolve o JWT
# Usa o formulário padrão do FastAPI para ler os dados enviados
@router.post("/token", response_model=Token)
def login_para_obter_token(session: SessionDep, dados_form: OAuth2PasswordRequestForm = Depends()):
    # Busca o usuário pelo campo username (que conterá o login)
    usuario = session.query(Usuarios).filter(Usuarios.login == dados_form.username).first()
    
    # Se o usuário não existir ou a senha hash não bater, barra o acesso
    if not usuario or not verificar_senha(dados_form.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Gera o token de acesso injetando o login no corpo do JWT
    token_jwt = criar_token_acesso(dados={"sub": usuario.login})
    
    return {"access_token": token_jwt, "token_type": "bearer"}