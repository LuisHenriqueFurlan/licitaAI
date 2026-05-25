UASGS = {

    "cuiaba": 153073,
    "brasilia": 110001,
    "sao paulo": 200100,
    "rio de janeiro": 170500

}


def buscar_uasg(cidade):

    if not cidade:

        return None

    cidade = cidade.lower().strip()

    return UASGS.get(
        cidade
    )