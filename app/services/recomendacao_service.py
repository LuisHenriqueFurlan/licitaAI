def gerar_recomendacao(economia):

    if economia > 1000:

        return (
            "Alta oportunidade: "
            "grande diferença entre "
            "mercado e governo."
        )

    elif economia > 0:

        return (
            "Média oportunidade: "
            "existe economia potencial."
        )

    return (

        "Baixa oportunidade: "
        "valor de mercado acima "
        "do valor estimado."

    )