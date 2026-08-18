# 🛒 API E-commerce Avançado — SENAI

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.11x-009688)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

## 📋 Sobre o Projeto

**Tema escolhido:** sistema de back-end completo para um e-commerce, responsável por gerenciar catálogo de produtos, categorias, carrinho de pedidos e autenticação de usuários.

Este projeto é o **Trabalho Final (TFU)** do **Módulo 5 — Desenvolvimento de API RESTful**, do curso SENAI. A API foi construída com **FastAPI** e **SQLAlchemy 2.0**, aplicando boas práticas de modelagem de dados, relacionamentos complexos e segurança na camada de autenticação.

### ✨ Principais características

- **Autenticação segura** de usuários com criptografia de senhas (hashing).
- **Modelagem relacional** com relacionamentos 1:N (produto ↔ categoria) e N:M (carrinho ↔ produtos).
- **Validação de dados** de entrada e saída com Pydantic.
- **Integridade referencial** garantida pelo ORM SQLAlchemy 2.0.
- **Documentação interativa** gerada automaticamente (Swagger UI e ReDoc).

---

## 🧱 Tecnologias Utilizadas

| Camada | Tecnologia |
|---|---|
| Framework web | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Validação de dados | Pydantic |
| Banco de dados | SQLite |
| Autenticação | Hash de senhas (Passlib / bcrypt) + JWT *(ajuste conforme implementação)* |
| Servidor ASGI | Uvicorn (via `fastapi dev`) |

> ⚠️ Ajuste a tabela acima com o banco de dados e o mecanismo de autenticação exatos usados no projeto, caso sejam diferentes do indicado.

---

## 📂 Funcionalidades Principais

- **Usuários:** cadastro, autenticação e gerenciamento de contas.
- **Categorias:** criação, listagem, atualização e exclusão de categorias de produtos.
- **Produtos:** CRUD completo, vinculado a uma categoria.
- **Carrinho de pedidos:** adição e remoção de produtos, cálculo de totais e finalização de pedido.

---

## 🛠️ Como Instalar e Executar

### Pré-requisitos

- [Python 3.11+](https://www.python.org/downloads/) instalado
- [Git](https://git-scm.com/) instalado

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

No Windows:
```bash
.venv\Scripts\activate
```

No Linux/Mac:
```bash
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie as tabelas do banco de dados

```bash
python tfu/criar_tabelas.py
```

### 5. Execute o projeto

```bash
fastapi dev tfu/main.py
```

O servidor será iniciado em modo de desenvolvimento, com *reload* automático a cada alteração de código.

---

## 📖 Documentação da API

Após iniciar o servidor, a documentação interativa fica disponível em:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📁 Estrutura do Projeto

```
├── tfu/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── criar_tabelas.py     # Script de criação das tabelas no banco
│   ├── dependencias.py      # Dependências injetáveis (Depends) da API
│   ├── excecoes.py          # Exceções customizadas da aplicação
│   ├── models/              # Modelos SQLAlchemy (entidades)
│   ├── schemas/             # Schemas Pydantic (validação)
│   ├── routers/             # Rotas/endpoints da API
│   ├── utils/               # Funções utilitárias e auxiliares
│   └── database.py          # Configuração de conexão com o banco
├── requirements.txt
└── README.md
```


---

Desenvolvido como Trabalho Final do Módulo 5 do curso **SENAI — Desenvolvimento de API RESTful**.