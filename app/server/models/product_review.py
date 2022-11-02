from datetime import datetime

from pydantic import BaseModel
from typing import Optional

class ProductReview(BaseModel):
    name : str
    product : str
    rating : float
    review : str
    date : datetime.now()
    class Settings:
        name = "product_review"
        
    class Config:
        scema_extra = {
            "example" : {
                "name" : "jhhwang",
                "product" : "TestDriven TDD Course",
                "rating" : 4.9,
                "review" : "Umm...",
                "date" : datetime.now()
            }
        }