from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema import CarFeatures, PredictResponse
from model import predict_price, load_artifacts

app = FastAPI(
    title="Car Price Prediction API",
    description="Predict the price of a used car",
    version="1.0.0",
    docs_url="/docs",
)


@app.on_event("startup")
def startup_event():
    load_artifacts()


@app.get("/")
def test():
    return JSONResponse(status_code=200, content={"success": True})


@app.post("/predict", response_model=PredictResponse)
def predict(features: CarFeatures):
    price = predict_price(features.model_dump())
    return PredictResponse(prediction_price=price)
