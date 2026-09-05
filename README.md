# Conversor de Moedas - FastAPI

API feita em Python com FastAPI que converte valores entre moedas usando cotação real, puxando os dados da AwesomeAPI.

## O que faz

- Converte um valor de uma moeda pra outra usando a cotação atual
- Valida se o valor digitado é positivo
- Trata erro caso a moeda não exista ou a API externa falhe

## Tecnologias usadas

- Python 3.13
- FastAPI
- Requests
- Uvicorn

## Como rodar o projeto

Clone o repositório:

git clone https://github.com/Luisgnvst/conversor-moedas-fastapi.git
cd conversor-moedas-fastapi


Crie um ambiente virtual e ative (opcional):

python -m venv .venv
.venv\Scripts\activate


Instale as dependências:

pip install fastapi uvicorn requests


Suba o servidor:

uvicorn main:app --reload


A API vai estar disponível em http://127.0.0.1:8000

## Como usar

Rota: GET /converter

Parâmetros:
- de: moeda de origem (ex: USD)
- para: moeda de destino (ex: BRL)
- valor: valor a converter

Exemplo:

GET /converter?de=USD&para=BRL&valor=10


Resposta de sucesso:

{"resultado": 54.0}


Resposta se o valor for inválido:

{"erro": "Voce colocou um valor errado, digite novamente!"}


Resposta se a moeda for inválida ou a API externa falhar:

{"erro": "Voce colocou algo errado, confira e atualize novamente"}


## Autor

Luis Gabriel

GitHub: https://github.com/Luisgnvst

LinkedIn: https://www.linkedin.com/in/luis-gabriel-neves-trist%C3%A3o-068a772b7/
