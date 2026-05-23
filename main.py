from fastapi import FastAPI
from app.routes.home import router
from app.routes.pregoes import router as pregoes_router

app = FastAPI()

app.include_router(router)
app.include_router(pregoes_router)