import uvicorn
from config import initiate_database
from fastapi import FastAPI
from routes import router as ProductRoute

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Products"}


app.include_router(ProductRoute, tags=["Products"], prefix="/product")
