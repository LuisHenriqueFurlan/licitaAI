from fastapi import APIRouter

from app.services.database_service import (
    listar_pregoes
)

from app.services.dashboard_service import (
    gerar_dashboard
)

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    dados = listar_pregoes()

    return gerar_dashboard(
        dados
    )