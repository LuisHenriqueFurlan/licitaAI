def calcular_score(itens, categoria):

    score = 0


    score += len(itens) * 5


    for item in itens:

        try:

            valor = float(
                item.get(
                    "valor_estimado",
                    0
                )
            )

            score += valor / 1000

        except:

            pass


    if categoria == "Tecnologia":

        score += 30


    elif categoria == "Hospitalar":

        score += 20


    elif categoria == "Automotivo":

        score += 15


    score = min(
        round(score),
        100
    )


    return score