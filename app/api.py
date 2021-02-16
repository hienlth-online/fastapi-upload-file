from fastapi import FastAPI, File, UploadFile
from typing import List
import shutil
import os

app = FastAPI()

UPLOAD_DIRECTORY = os.getcwd()

@app.post("/image", tags=["UploadFile"])
async def image(image: UploadFile = File(...)):
    with open(os.path.join(UPLOAD_DIRECTORY, "data", image.filename), "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}


@app.post("/images", tags=["UploadFile"])
async def images(images: List[UploadFile] = File(...)):
    for image in images:
        with open(os.path.join(UPLOAD_DIRECTORY, "data", image.filename), "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)