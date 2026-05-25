import requests

from collections import defaultdict

from app.services.classificador_service import (
    classificar_pregao
)

from app.services.score_service import (
    calcular_score
)

from app.services.resumo_service import (
    gerar_resumo
)

from app.services.oportunidade_service import (
    calcular_oportunidade
)

from app.services.preco_service import (
    buscar_menor_preco
)

from app.services.recomendacao_service import (
    gerar_recomendacao
)

from app.services.database_service import (
    salvar_pregao
)



def buscar_pregoes(
        cidade=None,
        uasg=None
):

    try:

        url = (
            "https://dadosabertos.compras.gov.br/"
            "modulo-legado/4_consultarItensPregoes"
        )


        params = {

            "pagina": 10,
            "tamanhoPagina": 10,

            "dt_hom_inicial": "2025-04-01",
            "dt_hom_final": "2025-05-01"

        }


        resposta = requests.get(

            url,

            params=params,

            timeout=30

        )


        dados = resposta.json()


        pregoes = defaultdict(
            list
        )


        for item in dados.get(

            "resultado",

            []

        ):

            pregao_id = item.get(
                "idCompra"
            )


            produto = item.get(
                "descricaoItem"
            )


            mercado = buscar_menor_preco(
                produto
            )


            valor_governo = float(

                item.get(
                    "valorEstimadoItem",
                    0
                )

            )


            menor_preco = (

                mercado.get(
                    "menor_preco",
                    {}
                )

                .get(
                    "preco",
                    0
                )

            )


            economia = round(

                valor_governo
                -
                menor_preco,

                2

            )


            recomendacao = gerar_recomendacao(
                economia
            )


            pregoes[pregao_id].append({

                "item_id":
                    item.get(
                        "idCompraItem"
                    ),

                "produto":
                    produto,

                "descricao":
                    item.get(
                        "descricaoDetalhadaItem"
                    ),

                "quantidade":
                    item.get(
                        "quantidadeItem"
                    ),

                "valor_governo":
                    valor_governo,

                "mercado":
                    mercado,

                "economia":
                    economia,

                "recomendacao":
                    recomendacao

            })



        resultado = []


        for pregao_id, itens in pregoes.items():

            categoria = classificar_pregao(
                itens
            )


            score = calcular_score(

                itens,

                categoria

            )


            resumo = gerar_resumo(

                itens,

                categoria

            )


            oportunidade = calcular_oportunidade(
                itens
            )


            prioridade = (

                "Alta"

                if score >= 70

                else

                "Média"

                if score >= 40

                else

                "Baixa"

            )


            if oportunidade == "Alta":

                try:

                    salvar_pregao({

                        "pregao_id":
                            pregao_id,

                        "categoria":
                            categoria,

                        "score":
                            score,

                        "prioridade":
                            prioridade,

                        "oportunidade":
                            oportunidade,

                        "resumo":
                            resumo

                    })

                except Exception as erro:

                    print(
                        "ERRO AO SALVAR:",
                        erro
                    )


            resultado.append({

                "pregao_id":
                    pregao_id,

                "categoria":
                    categoria,

                "score":
                    score,

                "prioridade":
                    prioridade,

                "oportunidade":
                    oportunidade,

                "resumo":
                    resumo,

                "quantidade_itens":
                    len(
                        itens
                    ),

                "itens":
                    itens

            })


        resultado.sort(

            key=lambda x:
            x["score"],

            reverse=True

        )


        return {

            "total_pregoes":
                len(
                    resultado
                ),

            "pregoes":
                resultado

        }


    except Exception as erro:

        return {

            "erro":
                str(
                    erro
                )

        }