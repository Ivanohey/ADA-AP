# install and import FastAPI and hypercorn libraries
# Hypercorn is an ASGI web server
# FastAPI is similar to Django, just a bit faster abd more modern
# read more about FastAPI here: https://towardsdatascience.com/create-your-first-rest-api-in-fastapi-e728ae649a60
from fastapi import FastAPI
from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import predict

class PictureModel(BaseModel):
    img: str

# === FastAPI configuration part ===
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# === FastAPI configuration part ===

# === Below some examples for RestAPI ===
@app.get("/")
async def root():
    print("Received GET request from frontend !")
    return {"message": "I'm getting this from server.py at localhost:8000 - function root"}


@app.post("/")
async def newRoot():
    print("Received POST request from frontend")
    return {"message": "I'm posting this from server.py at localhost:8000 - function newRoot"}


#API POST request, here the server receives a picture from the frontend and call predict.predict()
@app.get("/picture")
async def postPicture():
    print("Received POST resquest at /picture")
    return {"result": "test"}

# === Start server using hypercorn ===
asyncio.run(serve(app, Config()))
# === Start server using hypercorn ===


    