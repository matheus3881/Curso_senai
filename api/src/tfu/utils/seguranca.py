from datetime import datetime, timedelta, timezone
from typing import Optional
from passlib.context import CryptContext
import jwt

# Configurações de Criptografia
SECRET_KEY = "7c6b41ae4055ceaac8065158cd547245be8701eecba40316074709544dd9a26d"  # No mundo real, ficaria num arquivo .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para geração e verificação de hashes de senha (usando bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 1. Transforma a senha limpa em um Hash seguro para salvar no banco
def gerar_senha_hash(senha: str) -> str:
    return pwd_context.hash(senha)

# 2. Compara a senha digitada no login com o Hash salvo no banco
def verificar_senha(senha_pura: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_pura, senha_hash)

# 3. Gera o Token JWT contendo o login do usuário e tempo de expiração
def criar_token_acesso(dados: dict, tempo_expiracao: Optional[timedelta] = None) -> str:
    dados_para_criptografar = dados.copy()
    
    if tempo_expiracao:
        expire = datetime.now(timezone.utc) + tempo_expiracao
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    dados_para_criptografar.update({"exp": expire})
    token_jwt = jwt.encode(dados_para_criptografar, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt