# LicitaAI

Sistema inteligente para análise e apoio à tomada de decisão em pregões públicos utilizando automação, Machine Learning e Inteligência Artificial.

## Objetivo

O LicitaAI está sendo desenvolvido para auxiliar empresas que participam de licitações públicas, automatizando tarefas que normalmente são feitas manualmente.

Futuras funcionalidades:

- Análise automática de editais
- Extração de requisitos técnicos
- Busca inteligente de produtos
- Comparação de preços
- Recomendações baseadas em IA
- Predição de valores e estratégias de lance
- Dashboard de acompanhamento

---

## Tecnologias utilizadas

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

### Controle de versão
- Git
- GitHub

### Futuras tecnologias
- PostgreSQL
- OpenAI API
- Scikit-Learn
- Pandas
- React
- Docker

---

## Estrutura atual do projeto

```txt
LicitaAI/

app/
│
├── database/
│   ├── base.py
│   ├── connection.py
│   └── create_db.py
│
├── models/
│   └── pregao.py
│
├── routes/
│   ├── home.py
│   └── pregoes.py
│
├── schemas/
│   └── pregao_schema.py
│
├── services/
│   └── pregoes_service.py
│
├── __init__.py
│
├── .env
├── .gitignore
├── main.py
└── licitaai.db
```

---

## Arquitetura utilizada

O projeto segue separação por responsabilidades:

- **Routes**
    - Recebem as requisições da API

- **Services**
    - Contêm a lógica de negócio

- **Models**
    - Representam as tabelas do banco

- **Schemas**
    - Validam dados recebidos

- **Database**
    - Gerenciam conexão e configuração do banco

---

## Fluxo atual

```txt
Cliente
   ↓
FastAPI
   ↓
Pydantic (validação)
   ↓
Routes
   ↓
Services
   ↓
SQLAlchemy ORM
   ↓
SQLite
```

---

## Como executar o projeto

### Clonar repositório

```bash
git clone URL_DO_REPOSITORIO
```

### Entrar na pasta

```bash
cd LicitaAI
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Instalar dependências

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

### Criar banco

```bash
python -m app.database.create_db
```

### Executar aplicação

```bash
uvicorn main:app --reload
```

---

## Documentação automática

Após executar:

```txt
http://localhost:8000/docs
```

---

## Funcionalidades implementadas

- Estrutura inicial do projeto
- API com FastAPI
- Banco de dados SQLite
- ORM com SQLAlchemy
- Validação com Pydantic
- Cadastro de pregões
- Consulta de pregões
- Persistência de dados

---

## Status do projeto

Em desenvolvimento 🚧

Projeto desenvolvido para aprendizado prático de Engenharia de Software, APIs, Banco de Dados, IA e Automação.