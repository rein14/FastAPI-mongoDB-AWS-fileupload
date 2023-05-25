from typing import Optional

from beanie import init_beanie
from .models import Product
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None

    # aws
    AWS_ACCESS_ID: str
    AWS_ACCESS_KEY: str
    AWS_REGION: str
    BUCKET_NAME: str

    class Config:
        env_file = "app/.env"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient("mongodb://localhost:27017/product")
    await init_beanie(
        database=client.get_default_database(),
        document_models=[Product],
    )
