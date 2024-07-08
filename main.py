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
        hostname = socket.gethostbyname(url.split("//")[-1].split("/")[0])
        response = os.system(f"ping -n 1 {hostname}")
        if response == 0:
            logging.info(f"{hostname} is reachable")
            return True
        else:
            logging.error(f"{hostname} is not reachable")
            return False

    def fetch_data(self, url, method="GET", data=None, headers=None, timeout=10):
        if not self.ping_host(url):
            logging.error("Host is not reachable. Aborting request.")
            return

        try:
            response = self.session.request(method=method, url=url, data=data, headers=headers, timeout=timeout)
            self._handle_response(response)
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")

    def _handle_response(self, response):
        if response.ok:
            logging.info(f"Success! Status code: {response.status_code}")
        else:
            logging.error(f"Failed to fetch data. Status code: {response.status_code}")

        logging.info("Response Headers:")
        for key, value in response.headers.items():
            logging.info(f"{key}: {value}")
        
        logging.info("\nContent:")
        logging.info(response.text)


client = SimpleHttpClient()

# GET request
# client.fetch_data('https://fakestoreapi.com/products', 'GET')

# POST request with custom headers
# client.fetch_data('https://fakestoreapi.com/products', 'POST', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}), headers={"Content-Type": "application/json"})

# PUT request
# client.fetch_data('https://fakestoreapi.com/products/7', 'PUT', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}))

# DELETE request
client.fetch_data('https://fakestoreapi.com/products/7', 'DELETE')
