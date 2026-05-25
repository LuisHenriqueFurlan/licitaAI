def obter_peso(
    requisito: str
):

    pesos = {

        "ram":40,

        "ssd":30,

        "processador":20,

        "garantia":10,

        "marca":10
    }


    return pesos.get(

        requisito.lower(),

        5
    )