from typing import List

from fastapi import APIRouter
from schemas import ProductSchema
from services import FetcherService


api_fetcher_router = APIRouter()

@api_fetcher_router.get('/fetcher/fetch', response_model = List[ProductSchema.ProductData], tags=["Sorting Api"])
async def fetch_product_data():
    fetchResponseList = FetcherService.fetch_all_products()
    return fetchResponseList
