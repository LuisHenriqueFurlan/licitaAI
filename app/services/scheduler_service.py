from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.services.comprasgov_service import (
    buscar_pregoes
)


scheduler = (
    BackgroundScheduler()
)


def iniciar_scheduler():

    scheduler.add_job(

        buscar_pregoes,

        "interval",

        minutes=30

    )

    scheduler.start()

    print(
        "Scheduler iniciado"
    )