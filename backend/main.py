from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()

# Loading the model
model = YOLO(
    '/home/nyangweso/Desktop/Ds_1/Blood-Cell-Detection/data/processed_data/runs/detect/train/weights/best.pt')


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Reading the image file
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Performing object detection
    results = model(img)

    # Extracting the class of the detected object
    detected_class = results.xyxy[0][-1]

    return {"class": detected_class}
