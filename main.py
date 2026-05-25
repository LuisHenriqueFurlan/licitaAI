from fastapi import FastAPI
from app.routes.home import router
from app.routes.pregoes import router as pregoes_router
from app.routes.edital import router as edital_router
from app.routes.produtos import router as produtos_router
from app.routes.atributo import (
    router as atributos_router
)
from app.routes.busca import (
    router as busca_router
)
from app.routes.comparacao import (
    router as comparacao_router
)
from fastapi.middleware.cors import CORSMiddleware
from app.routes.comprasgov import (
    router as comprasgov_router
)
from app.routes.atualizacao import (
    router as atualizacao_router
)
from app.database.database import (
    criar_tabela
)
from app.routes.mercado import (
    router as mercado_router
)
from app.routes.precos import (
    router as preco_router
)



app = FastAPI()

criar_tabela()


app.include_router(router)
app.include_router(pregoes_router)
app.include_router(edital_router)
app.include_router(produtos_router)
app.include_router(atributos_router)
app.include_router(busca_router)
app.include_router(comparacao_router)
app.include_router(comprasgov_router)
app.include_router(atualizacao_router)
app.include_router(mercado_router)
app.include_router(preco_router)   


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)