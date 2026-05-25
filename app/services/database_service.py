from app.database.database import (
    conectar
)


def salvar_pregao(pregao):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT OR REPLACE INTO pregoes(

        pregao_id,
        categoria,
        score,
        prioridade,
        oportunidade,
        resumo

    )

    VALUES(
        ?,?,?,?,?,?
    )

    """,(

        pregao["pregao_id"],
        pregao["categoria"],
        pregao["score"],
        pregao["prioridade"],
        pregao["oportunidade"],
        pregao["resumo"]

    ))

    conn.commit()

    conn.close()



def listar_pregoes():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM pregoes"
    )

    dados = cursor.fetchall()

    conn.close()

    resultado=[]

    for item in dados:

        resultado.append({

            "pregao_id": item[0],
            "categoria": item[1],
            "score": item[2],
            "prioridade": item[3],
            "oportunidade": item[4],
            "resumo": item[5],
            "data_analise": item[6]

        })

    return resultado