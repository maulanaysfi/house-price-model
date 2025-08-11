from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import numpy as np
import os

model = joblib.load('app/house_price_model_v4.joblib')

class model_input(BaseModel):
    Area: int
    Room: int
    Parking: int
    Warehouse: int
    Elevator: int

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.isdir(static_dir):
    os.makedirs(static_dir)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get('/')
def index():
    with open(f"{static_dir}/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post('/predict')
def predict_price(input_data: model_input):
    data = np.array([[input_data.Area, input_data.Room, input_data.Parking,
                      input_data.Warehouse, input_data.Elevator]])
    prediction = model.predict(data)
    return {'predicted_price': prediction[0]}