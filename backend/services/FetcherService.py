import json
from typing import List

from schemas import ProductSchema
from schemas.ProductSchema import Root

goldPrice = 107.263

filename = "products.json"
#read and return all the products from the json file
def read_all_products():
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return [Root.from_dict(item) for item in data]

def fetch_all_products():
    response = []
    products = read_all_products()
    for productData in products:
        response.append({
            "name" : productData.name,
            "popularityScore" : productData.popularityScore,
            "weight": productData.weight,
            "price": calculate_product_price(productData),
            "images": {
                "yellow": productData.images.yellow,
                "rose": productData.images.rose,
                "white": productData.images.white,
            }
        })
    return response

def calculate_product_price(product: Root):
    return (product.popularityScore + 1) * product.weight * getGoldPrice()

def getGoldPrice():
    return goldPrice