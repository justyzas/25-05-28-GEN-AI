import requests
from rich import print

# Produktų gavimas
# v

# result = response.json()
# print(result)

# Atsakymo duomenys:
# print(response.status_code)
# print(response.headers)
# print(response.text)

# {
#     "id": 1,
#     "name": "product_name_1",
#     "price": 23.29,
#     "weight": 10.55,
#     "quantity_in_stock": 4
#   },


# Produkto sukūrimas
# response = requests.post("http://localhost:8000/products", json={
#                          "id": 9, "name": "Pomidorų padažas Felix", "price": 5.70, "quantity_in_stock": 70, "weight": 0.890})


# response = requests.get("http://localhost:8000/products/545")
# result = response.json()
# print(result)


# response = requests.post(
#     "http://localhost:11434/api/embeddings",
#     json={
#         "model": model,
#         "prompt": "1. Kelių eismo taisyklės nustato eismo keliais tvarką visoje Lietuvos Respublikos teritorijoje."
#     }
# )
