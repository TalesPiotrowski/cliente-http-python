import pip._vendor.requests as requests
import json

def fetch_data(url, method="GET", data=None):
    # Escolher o método de parâmetro para a requisição
    if method.upper() == "GET":
        response = requests.get(url)
    elif method.upper() == "POST":
        response = requests.post(url, data=data)
    elif method.upper() == "PUT":
        response = requests.put(url, data=data)
    elif method.upper() == "DELETE":
        response = requests.delete(url)
    else:
        print(f"Unsupported method: {method}")
        return

    if response.status_code == 200:
        print(f"\nSuccess! Status code: {response.status_code}")
    else:
        print(f"\nFailed to fetch data. Status code: {response.status_code}")

    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    
    print("\nContent:")
    print(response.text)

# Example usage
#fetch_data('https://fakestoreapi.com/products', 'GET')
#fetch_data('https://fakestoreapi.com/products', 'POST', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}))
#fetch_data('https://fakestoreapi.com/products/7', 'PUT', data=json.dumps({"title": 'test product', "price": 13.5, "description": 'lorem ipsum set', "image": 'https://i.pravatar.cc', "category": 'electronic'}))
fetch_data('https://fakestoreapi.com/products/6', 'DELETE')