from app.database.connection import engine
from app.database.base import Base
from app.models.analise_ia import AnaliseIA
from app.models.pregao import Pregao
from app.models.produto import Produto
from app.models.atributo_produto import AtributoProduto

Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso")