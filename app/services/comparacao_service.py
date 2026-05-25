def comparar_produtos(produto1, produto2):

    resultado = {

        "produto1": produto1,
        "produto2": produto2,
        "similaridade": 0

    }


    palavras1 = set(
        produto1.lower().split()
    )

    palavras2 = set(
        produto2.lower().split()
    )


    iguais = palavras1.intersection(
        palavras2
    )


    total = palavras1.union(
        palavras2
    )


    if len(total) > 0:

        similaridade = (

            len(iguais)
            /
            len(total)

        ) * 100


        resultado[
            "similaridade"
        ] = round(
            similaridade,
            2
        )


    return resultado