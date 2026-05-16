from pydantic import BaseModel, Annotated, Field
from enum import Enum


class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"


class SellerType(str, Enum):
    dealer = "Dealer"
    individual = "Individual"


class Transmission(str, Enum):
    manual = "Manual"
    automatic = "Automatic"


class CarFeatures(BaseModel):
    car_name: Annotated[
        str, Field(min_length=1, description="Name of the car", examples="swift")
    ]
    year: Annotated[int, Field(description="Year of the car", examples=2014)]
    selling_price: Annotated[
        float, Field(gt=0, description="Selling price of the car", examples=5.5)
    ]
    present_price: Annotated[
        float, Field(gt=0, description="Present price of the car", examples=6.5)
    ]
    kms_driven: Annotated[
        int, Field(gt=0, description="Kilometers driven", examples=50000)
    ]
    fuel_type: FuelType
    seller_type: SellerType
    transmission: Transmission
    owner: Annotated[int, Field(min_length=1, description="Owner", examples=1)]


class PredictResponse(BaseModel):
    prediction_price: Annotated[
        float, Field(gt=0, description="Predicted price of the car", examples=5.5)
    ]
