import pdfplumber
import tempfile
import re


def extrair_texto(caminho_pdf):

    texto = ""

    with pdfplumber.open(caminho_pdf) as pdf:

        for pagina in pdf.pages:

            texto += pagina.extract_text() or ""

    return texto


async def processar_edital(arquivo):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        conteudo = await arquivo.read()

        temp.write(conteudo)

        caminho = temp.name


    texto = extrair_texto(
        caminho
    )


    palavras_ruins = [

        "CERTIFICADO",
        "Autenticidade",
        "Certificamos",
        "Código",
        "FURLAN",
        "HENRIQUE",
        "Curso",
        "Conclusão"

    ]


    palavras = re.findall(

        r"\b[A-Z][a-zA-Z]{3,}\b",

        texto

    )


    palavras = list(
        set(
            palavras
        )
    )


    produtos=[]


    for palavra in palavras:

        if palavra not in palavras_ruins:

            produtos.append({

                "produto": palavra

            })


    return{

        "texto_extraido":

        texto[:500],

        "produtos":

        produtos[:10]

    }