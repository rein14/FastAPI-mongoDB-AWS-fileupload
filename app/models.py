from datetime import datetime
from typing import Optional, Any

from beanie import Document
from bson import ObjectId
from pydantic import BaseModel, root_validator


class Product(Document):
    name: str
    product_images: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_encoders = {
            ObjectId: str,
        }
        validate_assignment = True
        schema_extra = {
            "example": {
                "name": "Our Business",
                "product_images": "/file.png",
                "created_at": "2023-03-12T02:04:22.921+00:00",
                "updated_at": "2023-03-12T02:04:22.921+00:00",
            }
        }

    @root_validator
    def validate_updated_at(cls, values):
        "validate updated_at"
        if values["update_at"]:
            values["update_at"] = datetime.now()
        else:
            values["update_at"] = values["creaated_at"]
        return values


class Response(BaseModel):
    statusCode: int
    responseType: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "statusCode": 200,
                "responseType": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
