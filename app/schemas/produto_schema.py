from pydantic import BaseModel


class ProdutoCreate(BaseModel):

    nome: str
    preco: int


class CompararProduto(BaseModel):

    preco_maximo: int