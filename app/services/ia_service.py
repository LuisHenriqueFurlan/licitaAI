from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def analisar_edital(texto):

    resposta = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role":"system",

                "content": """
Extraia requisitos técnicos do edital.

Retorne APENAS JSON.

Exemplo:

{
"produto":"",
"processador":"",
"ram":"",
"ssd":"",
"garantia":""
}
"""
            },

            {
                "role":"user",
                "content": texto[:3000]
            }

        ]
    )

    return resposta.choices[0].message.content