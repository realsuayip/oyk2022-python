from fastapi import FastAPI

import pymongo

CONN_URL = "mongodb://mongodb:27017/?retryWrites=true&w=majority"

app = FastAPI()


@app.get("/")
async def root():
    client = pymongo.MongoClient(CONN_URL, serverSelectionTimeoutMS=5000)
    with client:
        return client.server_info()
