import sqlite3


def conectar():

    return sqlite3.connect(
        "licitai.db"
    )


def criar_tabela():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS pregoes(

        pregao_id TEXT PRIMARY KEY,

        categoria TEXT,

        score INTEGER,

        prioridade TEXT,

        oportunidade TEXT,

        resumo TEXT,

        data_analise TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()