def calcular_oportunidade(itens):

    total = 0

    for item in itens:

        try:

            valor = float(
                item.get(
                    "valor_estimado",
                    0
                )
            )

            total += valor

        except:

            pass


    if total > 5000:

        return "Alta"

    elif total > 2000:

        return "Média"

    return "Baixa"