from pydantic import BaseModel


class PregaoCreate(BaseModel):

    produto: str
    valor_referencia: int