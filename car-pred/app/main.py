from fastapi import FastAPI
from app.schema import CarFeatures, PredictResponse
from app.model import predict_price, load_artifacts

app = FastAPI(
    title="Car Price Prediction API",
    description="Predict the price of a used car",
    version="1.0.0",
    docs_url="/docs",
)