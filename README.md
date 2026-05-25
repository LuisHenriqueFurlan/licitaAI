# LicitaAI

Sistema inteligente para análise de editais e recomendação automática de produtos utilizando Inteligência Artificial.

O objetivo do projeto é automatizar parte do processo de leitura de editais, identificar requisitos técnicos e comparar com produtos cadastrados, gerando um ranking de compatibilidade.

---

## Funcionalidades atuais

✔ Upload de PDF de edital

✔ Extração automática de texto

✔ Identificação do produto solicitado

✔ Extração de requisitos técnicos

✔ Armazenamento em banco SQLite

✔ Cadastro automático de atributos

✔ Sistema de pesos para requisitos

✔ Comparação de produtos

✔ Ranking por compatibilidade

✔ Interface React moderna

✔ Integração preparada para OpenAI

---

## Tecnologias utilizadas

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- OpenAI API (estrutura pronta)
- PyPDF

### Frontend

- React
- Vite
- Axios
- Lucide Icons
- CSS

---

## Estrutura do projeto

```txt
licitaAI/

├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   │
│   ├── ia_service.py
│   ├── comparacao_service.py
│   ├── produto_service.py
│   ├── prompts_service.py
│
├── frontend/
│   ├── src/
│   ├── public/
│
├── licitaai.db
├── main.py
├── .env
└── README.md
```

---

## Como executar

### Clonar projeto

```bash
git clone https://github.com/SEU-USUARIO/licitaAI.git
```

Entrar na pasta:

```bash
cd licitaAI
```

---

## Backend

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar:

Windows:

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar:

```bash
uvicorn main:app --reload
```

Servidor:

```txt
http://localhost:8000
```

Swagger:

```txt
http://localhost:8000/docs
```

---

## Frontend

Entrar na pasta:

```bash
cd frontend
```

Instalar dependências:

```bash
npm install
```

Executar:

```bash
npm run dev
```

Frontend:

```txt
http://localhost:5173
```

---

## Fluxo do sistema

1. Usuário envia PDF

2. Sistema extrai texto

3. IA identifica requisitos técnicos

4. Dados são salvos no banco

5. Produtos são comparados

6. Sistema gera ranking

7. Resultado é exibido na interface

---

## Próximas etapas

- Integração real com OpenAI
- Histórico de análises
- Dashboard
- Login de usuários
- Upload drag-and-drop
- Exportar PDF
- Busca automática de produtos online
- Deploy

---

## Objetivo do projeto

Projeto desenvolvido para estudo de:

- Engenharia de Software
- APIs REST
- Inteligência Artificial
- Machine Learning
- Banco de dados
- Arquitetura Backend
- Desenvolvimento Full Stack

---

## Autor

Luis Henrique Furlan

Engenharia de Software