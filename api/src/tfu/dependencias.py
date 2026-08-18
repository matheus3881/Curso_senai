from fastapi import Query

class Paginacao:
    def __init__(
        self, 
        skip: int = Query(0, ge=0, description="Número de registros a pular"), 
        limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a retornar")
    ):
        self.skip = skip
        self.limit = limit