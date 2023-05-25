# fastAPI-mongoDB-AWS-fileupload

This is my take on uploading multiple files to AWS with fastAPI and mongoDB(beanie)

## Poetry
Create the virtual environment and install dependencies with:

> run poetry install

See https://python-poetry.org/docs/ the poetry docs for more information

### How to run? 
> poetry run uvicorn app:app --reload --host localhost --port 8000

API will be available at localhost:8000/
* Swagger UI docs at localhost:8000/docs
* ReDoc docs at localhost:8000/redoc

## Requirements
* fastAPI
* uvicorn[standard]
* beanie
* boto3