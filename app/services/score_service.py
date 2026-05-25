def calcular_score(itens, categoria):

    score = 50


    quantidade = len(itens)

    if quantidade > 10:
        score += 10

    elif quantidade > 5:
        score += 5


    economia_total = sum(
        item.get(
            "economia",
            0
        )
        for item in itens
    )


    if economia_total > 5000:

        score += 30

    elif economia_total > 2000:

        score += 20

    elif economia_total > 500:

        score += 10


    categorias_importantes = [

        "Tecnologia",
        "Automotivo",
        "Saúde"

    ]


    if categoria in categorias_importantes:

        score += 15


    return min(
        score,
        100
    )