def gerar_resumo(itens, categoria):

    quantidade = len(itens)

    produtos = []


    for item in itens:

        produto = item.get(
            "produto",
            ""
        )

        if produto not in produtos:

            produtos.append(
                produto
            )


    produtos_texto = ", ".join(
        produtos[:3]
    )


    resumo = (

        f"Pregão da categoria "
        f"{categoria} com "
        f"{quantidade} itens. "
        f"Principais produtos: "
        f"{produtos_texto}."

    )


    return resumo