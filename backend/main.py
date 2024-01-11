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
    nparr = np.frombuffer(contents, np.uint8)
    # nparr = np.fromstring(contents.decode("utf-8"), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    print('ok')
    # Performing object detection
    print(model(img))  # Returns a list of Results objects
#
#    with open("results.txt", "w") as f:
#        f.write(str(results))  # Replace content with your formatted information
#        f.close()
#    if results[0].probs is not None:
#        detected_class = results[0].probs.argmax()
#    else:
#        detected_class = None  # Handle the case of no detections
#
#    # Map index to class name if available
#    class_values = {
#        1: 'Band_Neutrophils',
#        2: 'Dyplastic_Cell',
#        3: 'Giant_Platelet',
#        4: 'Lymphoblast',
#        5: 'Lymphocytes',
#        6: 'Neutrophil',
#        7: 'Promyelocytes',
#        8: 'monocytes',
#        9: 'myelocytes',
#        10: 'not_cell',
#        11: 'nucleated_RBC'
#    }
#
#    return {"class_index": detected_class, "class_name": class_values}
