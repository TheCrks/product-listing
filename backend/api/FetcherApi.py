from typing import List

from fastapi import APIRouter
from schemas import ProductSchema
from services import FetcherService


api_fetcher_router = APIRouter()

@api_fetcher_router.get('/fetcher/fetch', response_model = List[ProductSchema.ProductData], tags=["Fetching Api"])
async def fetch_product_data():
    fetchResponseList = FetcherService.fetch_all_products()
    return fetchResponseList

@api_fetcher_router.post('/fetcher/filter', response_model = ProductSchema.FilterResponse, tags=["Fetching Api"])
async def fetch_product_filter(body: ProductSchema.FilterSchema):
    filterResponse = FetcherService.fetch_with_filter(body)
    return filterResponse