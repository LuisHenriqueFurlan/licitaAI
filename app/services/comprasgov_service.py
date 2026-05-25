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


def buscar_pregoes():

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

        print(
            "STATUS:",
            resposta.status_code
        )

        dados = resposta.json()

        pregoes = defaultdict(list)


        for item in dados.get(
            "resultado",
            []
        ):

            pregao_id = item.get(
                "idCompra"
            )

            pregoes[pregao_id].append({

                "item_id":
                    item.get(
                        "idCompraItem"
                    ),

                "produto":
                    item.get(
                        "descricaoItem"
                    ),

                "descricao":
                    item.get(
                        "descricaoDetalhadaItem"
                    ),

                "quantidade":
                    item.get(
                        "quantidadeItem"
                    ),

                "valor_estimado":
                    item.get(
                        "valorEstimadoItem"
                    ),

                "fornecedor":
                    item.get(
                        "fornecedorVencedor"
                    )

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

        print(
            "ERRO:",
            erro
        )

        return {

            "erro":
                str(
                    erro
                )

        }