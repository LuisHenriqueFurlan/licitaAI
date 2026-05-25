from sqlalchemy.orm import Session

from app.models.produto import Produto
from app.models.atributo_produto import (
    AtributoProduto
)

from app.services.pesos_service import (
    obter_peso
)


def comparar_valores(
    nome_requisito,
    valor_edital,
    valor_produto
):

    valor_edital = str(
        valor_edital
    ).lower()

    valor_produto = str(
        valor_produto
    ).lower()


    # comparação padrão
    if valor_edital in valor_produto:

        return True


    # regra especial: garantia mínima
    if nome_requisito == "garantia":

        try:

            edital = int(

                valor_edital.replace(
                    "meses",
                    ""
                )
            )

            produto = int(

                valor_produto.replace(
                    "meses",
                    ""
                )
            )

            return produto >= edital

        except:

            return False


    return False


def comparar_produtos(
    db: Session,
    requisitos: dict,
    preco_maximo=None
):

    produtos = db.query(
        Produto
    ).all()

    resultados = []


    for produto in produtos:

        atributos = db.query(
            AtributoProduto
        ).filter(

            AtributoProduto.produto_id
            == produto.id

        ).all()


        atributos_dict = {

            atributo.nome.lower():

            atributo.valor

            for atributo in atributos
        }


        peso_total = 0

        peso_obtido = 0


        # filtro por preço
        if preco_maximo:

            if produto.preco > preco_maximo:

                continue


        for nome, valor in requisitos.items():

            nome = nome.lower()

            peso = obter_peso(
                nome
            )

            peso_total += peso


            if nome in atributos_dict:

                if comparar_valores(

                    nome,

                    valor,

                    atributos_dict[
                        nome
                    ]
                ):

                    peso_obtido += peso


        compatibilidade = 0


        if peso_total > 0:

            compatibilidade = (

                peso_obtido /

                peso_total

            ) * 100


        resultados.append({

            "produto_id":
            produto.id,

            "nome":
            produto.nome,

            "preco":
            produto.preco,

            "compatibilidade":
            round(
                compatibilidade,
                2
            )
        })


    
    resultados = [

        resultado

        for resultado in resultados

        if resultado[
            "compatibilidade"
        ] > 0
    ]


    
    resultados.sort(

        key=lambda x:
        x["compatibilidade"],

        reverse=True
    )


    return resultados