from pydantic import BaseModel


class ResultadoComparacao(
    BaseModel):

    produto_id: int

    nome: str

    compatibilidade: float