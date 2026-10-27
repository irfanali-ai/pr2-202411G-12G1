# import requests
# url = "https://dummyjson.com/products"
# response = requests.get(url)
# data = response.json()
# for product in data["products"]:
#     print(product["price"], end=" ")

import requests

# url = "https://dummyjson.com/products/add"
# product = {
#     "title":"My Laptop",
#     "Price":4500.6
# }
# r = requests.post(url, json=product)
# print(r.status_code)
# print(r.json())


# url = "https://dummyjson.com/products/1"
# product = {
#     "title":"Update data",
#     "price":5000
# }
# r = requests.put(url, json=product)
# print(r.status_code)
# print(r.json())

url = "https://dummyjson.com/products/1"
r = requests.delete(url)
print(r.status_code)
# r = requests.get("https://dummyjson.com/products")
# data = r.json()
# for product in data["products"]:
#     if product["title"] == "My laptop":
#         print(product)
#     else:
#         print("not found!")


