from pydantic import BaseModel


class AtributoCreate(BaseModel):

    produto_id: int
    nome: str
    valor: str