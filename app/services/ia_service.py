from app.services.prompts_service import (
    prompt_extracao_edital
)


def analisar_edital_ia(
    texto: str
):

    prompt = prompt_extracao_edital()

    print(
        "Prompt carregado"
    )

    print(
        prompt[:200]
    )


    # Simulação temporária
    # Depois será OpenAI real

    return {

        "produto":"Notebook",

        "requisitos":{

            "RAM":"16GB",

            "SSD":"512GB",

            "Processador":"i5"
        }
    }