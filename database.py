from datetime import datetime

from models import Product


async def add_product(
    name: str,
    product_image: str,
) -> Product:
    """Add a new product
    Arguments: name, product_image
    Return: product: Product"""
    product = Product(
        name=name,
        product_images=product_image,
    )

    new_product = await product.create()
    return new_product
