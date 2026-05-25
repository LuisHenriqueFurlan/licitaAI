from pydantic import BaseModel
from typing import Dict


class CompararProduto(BaseModel):

    preco_maximo: int

    requisitos: Dict[str, str]


class ResultadoComparacao(BaseModel):

    produto_id: int

    nome: str

    compatibilidade: float