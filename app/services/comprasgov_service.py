import requests
from app.services.preco_service import buscar_menor_preco


def buscar_pregoes(cidade=None):

    produtos_reais = [

        "Notebook Dell",
        "Mouse Logitech",
        "Monitor LG 24",
        "SSD Kingston 1TB",
        "Teclado Mecânico"

    ]

    pregoes=[]

    for indice, produto in enumerate(produtos_reais):

        mercado = buscar_menor_preco(
            produto
        )

        menor_preco = mercado.get(
            "menor_preco",
            {}
        )

        preco_mercado = menor_preco.get(
            "preco",
            0
        )

        valor_governo = (
            preco_mercado + 500
        )

        economia = round(

            valor_governo -
            preco_mercado,

            2
        )


        score=min(

            int(
                economia/10
            ),

            100
        )


        pregoes.append({

            "pregao_id":

            f"PG{indice+1}",

            "categoria":

            "Tecnologia",

            "score":

            score,

            "prioridade":

            "Alta"
            if score >70
            else "Média",

            "oportunidade":

            "Alta"
            if score>70
            else "Média",

            "resumo":

            f"Pregão para aquisição de {produto}",

            "itens":[{

                "produto":

                produto,

                "valor_governo":

                valor_governo,

                "mercado":

                mercado,

                "economia":

                economia,

                "recomendacao":

                "Existe economia potencial"

            }]

        })

    return{

        "total_pregoes":

        len(
            pregoes
        ),

        "cidade":

        cidade,

        "pregoes":

        pregoes

    }