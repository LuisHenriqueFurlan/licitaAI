import os

from serpapi.google_search import GoogleSearch
from dotenv import load_dotenv

load_dotenv()


def buscar_menor_preco(produto):

    try:

        api_key = os.getenv(
            "SERP_API_KEY"
        )

        if not api_key:

            return {

                "erro":
                    "SERP_API_KEY não encontrada"

            }


        params = {

            "engine":
                "google_shopping",

            "q":
                produto,

            "api_key":
                api_key,

            "gl":
                "br",

            "hl":
                "pt-br"

        }


        busca = GoogleSearch(
            params
        )

        resultados = busca.get_dict()

        produtos=[]


        for item in resultados.get(
            "shopping_results",
            []
        )[:10]:

            try:

                preco = item.get(
                    "extracted_price"
                )

                if preco is None:

                    preco = item.get(
                        "price"
                    )

                    if preco:

                        preco = str(
                            preco
                        )

                        preco = preco.replace(
                            "R$",
                            ""
                        )

                        preco = preco.replace(
                            ".",
                            ""
                        )

                        preco = preco.replace(
                            ",",
                            "."
                        )

                        preco=float(
                            preco.strip()
                        )


                if preco is None:
                    continue


                produtos.append({

                    "loja":
                        item.get(
                            "source",
                            "Desconhecida"
                        ),

                    "preco":
                        preco,

                    "titulo":
                        item.get(
                            "title"
                        ),

                    "link":
                        item.get(
                            "link"
                        )

                })

            except Exception as erro_item:

                print(
                    "ERRO ITEM:",
                    erro_item
                )


        if len(produtos)==0:

            return {

                "produto":
                    produto,

                "erro":
                    "Nenhum preço encontrado"

            }


        menor=min(

            produtos,

            key=lambda x:
            x["preco"]

        )


        return {

            "produto":
                produto,

            "menor_preco":
                menor,

            "comparacao":
                produtos

        }


    except Exception as erro:

        return {

            "erro":
                str(
                    erro
                )

        }