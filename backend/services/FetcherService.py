import json
from typing import List

import httpx
import os
from dotenv import load_dotenv

from schemas import ProductSchema
from schemas.ProductSchema import Root, FilterSchema, ProductData, FilterResponse

load_dotenv()
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

#fetch gold price as USD using goldapi
def getGoldPrice() -> float:
    GOLD_API_KEY = os.getenv("GOLD_API_KEY")
    GOLD_API_URL = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = httpx.get(GOLD_API_URL, headers=headers, timeout=5.0)
        if response.status_code == 200:
            data = response.json()
            price = data.get("price_gram_24k")
            if isinstance(price, (int, float)):
                return float(price)
    except Exception:
        print("Error fetching gold price, returning failsafe value: " + str(goldPrice))  # silently fail and use fallback

    return goldPrice  # fallback to hardcoded value

#returns products according to given filter
def fetch_with_filter(body: FilterSchema) -> FilterResponse:
    raw_products = fetch_all_products()
    response = FilterResponse(result="", data=[])

    try:
        # Convert raw dicts to ProductData instances
        products = [ProductData(**p) if isinstance(p, dict) else p for p in raw_products]

        param = body.parameter

        def compare(product_value):
            # Attempt to convert both to float if possible, else compare as strings
            try:
                return float(body.range_min) <= float(product_value) <= float(body.range_max)
            except (ValueError, TypeError):
                return str(body.range_min) <= str(product_value) <= str(body.range_max)

        filtered = [
            product for product in products
            if hasattr(product, param) and compare(getattr(product, param))
        ]

        response.result = "Success"
        response.data = filtered
        return response

    except Exception as e:
        print("Error Filtering:" + str(e))
        response.result = "Failed"
        response.data = raw_products
        return response


