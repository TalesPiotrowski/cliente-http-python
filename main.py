from pythonping import ping
import requests
import json
import logging
import os
import socket

class SimpleHttpClient:
    def __init__(self):
        self.session = requests.Session()
        logging.basicConfig(level=logging.INFO)

    def ping_host(self, url):
        # Extrai o nome do host da URL
        hostname = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(hostname)
        try:
            # Executa o ping para o hostname
            response = ping(ip_address, count=4, timeout=1)  
            # Calcula o número de pacotes recebidos com base nos resultados de sucesso
            packets_received = sum(1 for reply in response if reply.success)
            lost_packets = 4 - packets_received
            # Calcula o RTT médio para os pacotes recebidos
            rtt_avg_ms = sum(reply.time_elapsed for reply in response if reply.success) / packets_received * 1000 if packets_received > 0 else 0
            # Simula ou extrai o valor TTL (isso é um placeholder)
            ttl_value = 64  
            if packets_received > 0:
                logging.info(f"{hostname} ({ip_address}) é alcançável. RTT: {rtt_avg_ms:.2f}ms, Pacotes perdidos: {lost_packets}, TTL: {ttl_value}")
                return True
            else:
                logging.error(f"{hostname} ({ip_address}) não é alcançável. Pacotes perdidos: {lost_packets}, TTL: {ttl_value}")
                return False
        except Exception as e:
            logging.error(f"Falha ao fazer ping em {hostname} ({ip_address}): {e}")
            return False

    def fetch_data(self, url, method="GET", data=None, headers=None, timeout=10):
        if not self.ping_host(url):
            logging.error("Host não é alcançável. Abortando requisição.")
            return

        try:
            # Realiza a requisição HTTP
            response = self.session.request(method=method, url=url, data=data, headers=headers, timeout=timeout)
            # Manipula a resposta da requisição
            self._handle_response(response)
        except requests.RequestException as e:
           logging.error(f"Falha na requisição: {e}")

    def _handle_response(self, response):
        # Verifica a resposta:
        if response.ok:
            logging.info(f"Sucesso! Código de status: {response.status_code}")
        else:
            logging.error(f"Falha ao buscar dados. Código de status: {response.status_code}")

        logging.info("Cabeçalhos da Resposta:")
        for key, value in response.headers.items():
            logging.info(f"{key}: {value}")

        # Loga o conteúdo da resposta
        logging.info("\nConteúdo:")
        logging.info(response.text)

client = SimpleHttpClient()


# Requisição GET
#client.fetch_data('https://fakestoreapi.com/products', 'GET')

# Requisição POST com cabeçalhos personalizados
# client.fetch_data('https://fakestoreapi.com/products', 'POST', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}), headers={"Content-Type": "application/json"})

# Requisição PUT
# client.fetch_data('https://fakestoreapi.com/products/7', 'PUT', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}))

# Requisição DELETE
#chamada com erro de path product's'
client.fetch_data('https://fakestoreapi.com/product/7', 'DELETE')
