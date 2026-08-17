from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/produtos")

# ---------------------------- POST ------------------------ #
@router.post("/produtos", response_model=ProdutoResposta ,status_code=status.HTTP_201_CREATED)
def listar_produtos():
    pass

# ---------------------------- GET -------------------------- #
@router.get("", response_model=ProdutoResposta)
def listar_produtos():
    pass


@router.get("/{id_produto}", response_model=ProdutoResposta)
def buscar_produto(produto_id: int):
    pass

# ----------------------------- PUT -------------------------- #
@router.put("/{id_produto}", response_model=ProdutoResposta)
def atualizar_produto(produto_id: int):
    pass

# ---------------------------- PATCH -------------------------- #
@router.patch("/{id_produto}", response_model=ProdutoEntrada)
def alterar_produtos(produto_id: int):
    pass

# ---------------------------- DELETE -------------------------- #
@router.delete("/{id_produto}")
def remover_produtos(produto_id: int):
    pass

