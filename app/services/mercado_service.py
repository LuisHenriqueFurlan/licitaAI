import requests


def buscar_precos(produto):

    try:

        url = "https://api.mercadolibre.com/sites/MLB/search"

        resposta = requests.get(
            url,
            params={
                "q": produto
            },
            timeout=15
        )

        print("STATUS:", resposta.status_code)
        print("URL:", resposta.url)

        dados = resposta.json()

        resultados = []

        for item in dados.get(
            "results",
            []
        )[:5]:

            preco = item.get("price")

            if preco is None:
                continue

            resultados.append({

                "loja":
                    "Mercado Livre",

                "titulo":
                    item.get(
                        "title",
                        ""
                    ),

                "preco":
                    preco,

                "link":
                    item.get(
                        "permalink",
                        ""
                    )

            })


        if len(resultados) == 0:

            return {

                "produto":
                    produto,

                "erro":
                    "Nenhum produto encontrado",

                "resposta_api":
                    dados

            }


        menor = min(

            resultados,

            key=lambda x:
            x["preco"]

        )


        return {

            "produto":
                produto,

            "menor_preco":
                menor["preco"],

            "fonte":
                menor["loja"],

            "titulo":
                menor["titulo"],

            "link":
                menor["link"],

            "todos":
                resultados

        }

    except Exception as erro:

        return {

            "erro":
                str(erro)

        }