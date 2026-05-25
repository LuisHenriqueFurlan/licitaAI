CATEGORIAS = {

    "Tecnologia":[

        "notebook",
        "computador",
        "monitor",
        "mouse",
        "teclado",
        "servidor",
        "ssd",
        "hd",
        "memoria",
        "roteador",
        "switch",
        "impressora"

    ],

    "Hospitalar":[

        "hospital",
        "medicamento",
        "seringa",
        "agulha",
        "equipamento medico"

    ],

    "Automotivo":[

        "mola",
        "suspensao",
        "motor",
        "pneu",
        "freio",
        "veiculo"

    ],

    "Construção":[

        "cimento",
        "tijolo",
        "brita",
        "areia",
        "concreto"

    ]

}


def classificar_pregao(itens):

    texto = " ".join(

        [

            (

                str(
                    item.get(
                        "produto",
                        ""
                    )
                )

                +

                str(
                    item.get(
                        "descricao",
                        ""
                    )
                )

            ).lower()

            for item in itens

        ]

    )


    pontuacao = {}


    for categoria, palavras in CATEGORIAS.items():

        pontuacao[categoria] = 0


        for palavra in palavras:

            if palavra in texto:

                pontuacao[categoria] += 1


    melhor = max(
        pontuacao,
        key=pontuacao.get
    )


    if pontuacao[melhor] == 0:

        return "Outros"


    return melhor