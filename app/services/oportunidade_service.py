def calcular_oportunidade(itens):

    economia_total = sum(

        item.get(
            "economia",
            0
        )

        for item in itens

    )


    if economia_total > 5000:

        return "Alta"

    elif economia_total > 1000:

        return "Média"

    return "Baixa"