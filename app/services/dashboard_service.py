from collections import Counter


def gerar_dashboard(dados):

    categorias = Counter(

        p["categoria"]

        for p in dados

    )


    return {

        "total_pregoes":

            len(dados),

        "alta":

            len(

                [

                    p

                    for p in dados

                    if p[
                        "oportunidade"
                    ]=="Alta"

                ]

            ),

        "media":

            len(

                [

                    p

                    for p in dados

                    if p[
                        "oportunidade"
                    ]=="Média"

                ]

            ),

        "baixa":

            len(

                [

                    p

                    for p in dados

                    if p[
                        "oportunidade"
                    ]=="Baixa"

                ]

            ),

        "categorias":

            dict(
                categorias
            )

    }