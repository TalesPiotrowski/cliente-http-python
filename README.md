# cliente-http-python
Trabalho para o curso de redes de computadores

## Descrição
Este projeto implementa um cliente HTTP simples em Python, capaz de realizar requisições GET, POST, PUT e DELETE. A aplicação permite configurar cabeçalhos personalizados e enviar dados no corpo da requisição, além de exibir as mensagens de respostas HTTP.

## Pré-requisitos
- Python 3.x
- Import `requests` (já está inclusa no pacote `pip._vendor.requests`)
- Import json

## Uso
Execute o script main.py com os parâmetros apropriados. Exemplos de uso:

Requisição GET -> #fetch_data('https://fakestoreapi.com/products', 'GET')

Requisição POST -> #fetch_data('https://fakestoreapi.com/products', 'POST', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}))

Requisição PUT -> #fetch_data('https://fakestoreapi.com/products/7', 'PUT', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}))

Requisição DELETE -> #fetch_data('https://fakestoreapi.com/products/6', 'DELETE')
