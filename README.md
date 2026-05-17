# AutoEstimate AI 🏎️

AutoEstimate AI is an intelligent web application and API that predicts the market selling price of used cars based on historical data.

The project is broken down into two main components:
1. **FastAPI Backend:** A high-performance REST API that processes vehicle features and runs them through a pre-trained Random Forest Regressor machine learning model.
2. **Streamlit Frontend:** A sleek, dark-mode user interface that allows users to easily input vehicle specifications and instantly receive a predicted market value.

---

## 📂 Project Structure

```text
Car Prediction Fast Api/
│
├── car-pred/
│   ├── cardekho_data (1).csv       # Original dataset
│   ├── train.py                    # Script used to train the Random Forest model
│   ├── random_forest_model.pkl     # Serialized machine learning model
│   ├── feature_columns.pkl         # Serialized training feature columns (for one-hot encoding alignment)
│   ├── requirements.txt            # Python package dependencies
│   │
│   └── app/                        # Main Application Code
│       ├── main.py                 # FastAPI application and endpoint routing
│       ├── model.py                # Preprocessing and ML prediction logic
│       ├── schema.py               # Pydantic data validation and schemas
│       └── app.py                  # Streamlit frontend UI
│
└── venv/                           # Virtual Environment
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository and navigate to the project directory
```bash
cd "Car Prediction Fast Api"
```

### 2. Activate the Virtual Environment
**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install all the required packages to run both the API and the UI:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

Because this project features both a backend API and a frontend UI, you will need to run **two separate terminal instances**.

### Step 1: Start the FastAPI Backend
Open your first terminal window, activate the virtual environment, and run:
```bash
# Navigate to the app directory
cd car-pred/app

# Start the FastAPI server in development mode
fastapi dev main.py
```
*The API will start running at `http://127.0.0.1:8000`*

### Step 2: Start the Streamlit Frontend
Open a **second** terminal window, activate the virtual environment, and run:
```bash
# Navigate to the app directory
cd car-pred/app

# Start the Streamlit user interface
python -m streamlit run app.py
```
*Your web browser will automatically open the UI at `http://localhost:8501`*

---

## ⚙️ API Documentation

Once your FastAPI backend is running, you can access the automatically generated interactive documentation by navigating to:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

### Endpoint: `/predict`
- **Method:** `POST`
- **Description:** Accepts JSON data containing car specifications and returns the predicted selling price.
- **Payload Example:**
```json
{
  "car_name": "swift",
  "year": 2015,
  "present_price": 5.5,
  "kms_driven": 35000,
  "fuel_type": "Petrol",
  "seller_type": "Dealer",
  "transmission": "Manual",
  "owner": 0
}
```
- **Response Example:**
```json
{
  "prediction_price": 4.15
}
```
