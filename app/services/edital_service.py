import pdfplumber


def extrair_texto(pdf_path):

    texto = ""

    with pdfplumber.open(pdf_path) as pdf:

        print(
            f"Quantidade de páginas: {len(pdf.pages)}"
        )

        for pagina in pdf.pages:

            conteudo = pagina.extract_text()

            print(conteudo)

            if conteudo:
                texto += conteudo

    return texto