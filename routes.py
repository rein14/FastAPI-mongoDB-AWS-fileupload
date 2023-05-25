from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Body, File, Request, UploadFile
from models import Product, Response
from upload import fileUrl, handle_file_upload
from database import add_product

router = APIRouter()


@router.post(
    "/",
    response_description="Product data added into the database",
    response_model=Response,
)
async def PostProduct(
    request: Request,
    name: str,
    files: List[UploadFile] = File(...),
):
    # For testing purposes
    product_images = await handle_file_upload(files)

    product = await add_product(name=name, product_image= await fileUrl(product_images))
    return {
        "statusCode": 200,
        "responseType": "success",
        "description": "Product created successfully",
        "data": {
            "[product]": product,
        },
    }
