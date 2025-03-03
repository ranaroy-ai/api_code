import logging
from fastapi import FastAPI

app = FastAPI()

def init():
    logging.info("Service initialized.")

@app.get("/")
def run():
    return {"message": "Hello from FastAPI!"}
#
