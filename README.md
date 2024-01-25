# API assíncrona com FastAPI

Este projeto é uma API assíncrona desenvolvida utilizando o framework FastAPI. A API oferece endpoints para gerenciar informações relacionadas a Atletas, Categorias e Centro de Treinamento.

## Stack Utilizada

- **Python**: Versão 3.8 ou superior
- **FastAPI**: [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- **Alembic**: [Documentação do Alembic](https://alembic.sqlalchemy.org/)
- **SQLAlchemy**: [Documentação do SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- **PostgreSQL**: Banco de dados utilizado

## Instalação

1. Clone o repositório:


git clone https://github.com/anselmoaxo/API-assincrona-com-FastAPI.git
cd API-assincrona-com-FastAPI

## Endpoints
### Atletas
**Listar todos os atletas:**
***Endpoint: http://127.0.0.1:8000/atletas/***
Método: GET

**Detalhes de um atleta específico:**
Endpoint: http://127.0.0.1:8000/atletas/{id}/
Método: GET

**Adicionar um novo atleta:**
Endpoint: http://127.0.0.1:8000/atletas/
Método: POST

**Atualizar informações de um atleta:**
Endpoint: http://127.0.0.1:8000/atletas/{id}/
Método: PATCH

**Excluir um atleta:**
Endpoint: http://127.0.0.1:8000/atletas/{id}/
Método: DELETE

### Categorias

**Listar todas as categorias:**
Endpoint: http://127.0.0.1:8000/categorias/
Método: GET

**Adicionar uma nova categoria:**
Endpoint: http://127.0.0.1:8000/categorias/
Método: POST

**Detalhes de uma categoria específica:**
Endpoint: http://127.0.0.1:8000/categorias/{id}/
Método: GET


### Centro de Treinamento

**Listar todos os centros de treinamento:**
Endpoint: http://127.0.0.1:8000/centros_treinamento/
Método: GET

**Adicionar um novo centro de treinamento:**
Endpoint: http://127.0.0.1:8000/centros_treinamento/
Método: POST

**Detalhes de um centro de treinamento específico:**
Endpoint: http://127.0.0.1:8000/centros_treinamento/{id}/
Método: GET


## Documentação da API
Acesse a documentação interativa da API em http://127.0.0.1:8000/docs para obter informações detalhadas sobre os endpoints, parâmetros e respostas
