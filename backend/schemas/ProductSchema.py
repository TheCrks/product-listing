from pydantic import BaseModel

from typing import Any
from dataclasses import dataclass
import json


#class for fetching images field from json
@dataclass
class Images:
    yellow: str
    rose: str
    white: str

    @staticmethod
    def from_dict(obj: Any) -> 'Images':
        _yellow = str(obj.get("yellow"))
        _rose = str(obj.get("rose"))
        _white = str(obj.get("white"))
        return Images(_yellow, _rose, _white)

#class for fetching product data fron json
@dataclass
class Root:
    name: str
    popularityScore: float
    weight: float
    images: Images

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _name = str(obj.get("name"))
        _popularityScore = float(obj.get("popularityScore"))
        _weight = float(obj.get("weight"))
        _images = Images.from_dict(obj.get("images"))
        return Root(_name, _popularityScore, _weight, _images)

#class to use for the FastAPI /fetch endpoint
class ProductData(BaseModel):
    name: str
    popularityScore: float
    weight: float
    images: dict[str, str]
    price: float

    class Config:
        json_schema_extra = {
            "example":{
                "name": "Engagement Ring 8",
                "popularityScore": 0.90,
                "weight": 3.7,
                "price": 110,
                "images": {
                    "yellow": "https://cdn.shopify.com/s/files/1/0484/1429/4167/files/EG115-100P-Y.jpg?v=1696596076",
                    "rose": "https://cdn.shopify.com/s/files/1/0484/1429/4167/files/EG115-100P-R.jpg?v=1696596151",
                    "white": "https://cdn.shopify.com/s/files/1/0484/1429/4167/files/EG115-100P-W.jpg?v=1696596147"
                }
            }
        }

