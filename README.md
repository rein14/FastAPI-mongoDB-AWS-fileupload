# fastAPI-mongoDB-AWS-fileupload

This is my take on uploading multiple files to AWS with fastAPI and mongoDB(beanie)

 ## How to run?

### Poetry
Create a virtual environment and install dependencies with:

> run poetry install
See the poetry docs for more information

Run commands inside the virtual environment with:

## How to run? 
> python main.py

Swagger UI docs at localhost:8000/docs
ReDoc docs at localhost:8000/redoc
To run testing/linting locally you would run lint/test in the scripts directory.

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