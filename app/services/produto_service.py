from sqlalchemy.orm import Session

from app.models.produto import Produto


def criar_produto(
    db: Session,
    nome: str,
    preco: int
):

    novo_produto = Produto(
        nome=nome,
        preco=preco
    )

    db.add(
        novo_produto
    )

    db.commit()

    db.refresh(
        novo_produto
    )

    return novo_produto


def listar_produtos(
    db: Session
):

    return db.query(
        Produto
    ).all()


def comparar_produtos(
    db: Session,
    preco_maximo: int
):

    produtos = db.query(
        Produto
    ).all()


    produtos_validos = []


    for produto in produtos:

        if produto.preco <= preco_maximo:

            produtos_validos.append(
                produto
            )


    return produtos_validos

from app.models.atributo_produto import (
    AtributoProduto
)


def comparar_requisitos(
    db: Session,
    preco_maximo: int,
    requisitos: dict
):

    produtos = db.query(
        Produto
    ).all()

    produtos_validos = []


    for produto in produtos:

        if produto.preco > preco_maximo:
            continue


        atributos = db.query(
            AtributoProduto
        ).filter(
            AtributoProduto.produto_id == produto.id
        ).all()


        atributos_dict = {}

        for atributo in atributos:

            atributos_dict[
                atributo.nome.lower()
            ] = atributo.valor.lower()


        atende = True


        for chave, valor in requisitos.items():

            if (
                chave.lower()
                not in atributos_dict
            ):

                atende = False
                break


            if (
                atributos_dict[
                    chave.lower()
                ]
                != valor.lower()
            ):

                atende = False
                break


        if atende:

            produtos_validos.append(
                produto
            )


    return produtos_validos

def buscar_ou_criar_produto(
    db: Session,
    nome: str,
    preco: int
):

    produto = db.query(
        Produto
    ).filter(
        Produto.nome == nome
    ).first()


    if produto:

        return produto


    novo_produto = Produto(

        nome=nome,
        preco=preco
    )


    db.add(
        novo_produto
    )

    db.commit()

    db.refresh(
        novo_produto
    )

    return novo_produto