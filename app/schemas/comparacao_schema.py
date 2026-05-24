from pydantic import BaseModel
from typing import Dict


class ComparacaoRequest(BaseModel):

    preco_maximo: int

    requisitos: Dict[str, str]