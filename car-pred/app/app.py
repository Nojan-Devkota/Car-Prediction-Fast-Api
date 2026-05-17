import streamlit as st
import requests

API_URL = "https://car-prediction-fast-api.onrender.com/predict"  # "http://127.0.0.1:8000/predict"

# ----------------- UI Config -----------------
st.set_page_config(page_title="AutoEstimate AI", page_icon="🏎️", layout="centered")

# ----------------- Custom CSS -----------------
st.markdown(
    """
<style>
    /* Global Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Title Styling */
    .title-text {
        text-align: center;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0px;
    }
    
    /* Subtitle Styling */
    .subtitle-text {
        text-align: center;
        color: #A0AEC0;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #FF4B4B 0%, #FF8E53 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: bold;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.5);
    }

    /* Prediction Result Box */
    .prediction-box {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 15px;
        padding: 40px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        animation: fadeIn 0.5s ease-in-out;
    }
    .price-text {
        font-size: 4.5rem;
        font-weight: 900;
        color: #10B981;
        margin: 0;
        text-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""",
    unsafe_allow_html=True,
)

# ----------------- Header -----------------
st.markdown('<h1 class="title-text">AutoEstimate AI</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle-text">Get hyper-accurate market value predictions for your used car</p>',
    unsafe_allow_html=True,
)

# ----------------- Input Form -----------------
st.markdown("### 🚘 Vehicle Specifications")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    car_name = st.text_input("Car Model Name", placeholder="e.g. Swift, City, i20")
    year = st.number_input(
        "Manufacture Year", min_value=1990, max_value=2024, value=2015, step=1
    )
    present_price = st.number_input(
        "Current Showroom Price (Lakhs)",
        min_value=0.1,
        max_value=100.0,
        value=5.5,
        step=0.1,
    )
    kms_driven = st.number_input(
        "Kilometers Driven", min_value=0, max_value=500000, value=35000, step=1000
    )

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner = st.number_input(
        "Number of Previous Owners", min_value=0, max_value=5, value=0, step=1
    )

# ----------------- Prediction Logic -----------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("Calculate Market Value"):
    if not car_name.strip():
        st.error("⚠️ Please enter the car model name.")
    else:
        # Build JSON Payload matching our Pydantic Schema
        payload = {
            "car_name": car_name,
            "year": year,
            "present_price": present_price,
            "kms_driven": kms_driven,
            "fuel_type": fuel_type,
            "seller_type": seller_type,
            "transmission": transmission,
            "owner": owner,
        }

        # Send HTTP POST Request to FastAPI
        try:
            with st.spinner("Analyzing market data..."):
                response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                data = response.json()
                pred_price = data.get("prediction_price", 0)

                # Render Beautiful Result Box
                st.markdown(
                    f"""
                <div class="prediction-box">
                    <p style="color: #94A3B8; font-size: 1.2rem; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 2px;">Estimated Selling Price</p>
                    <h2 class="price-text">₹ {pred_price:.2f} Lakhs</h2>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                st.balloons()  # Fun micro-animation
            else:
                st.error(f"❌ Error from API: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error(
                "🚨 Could not connect to the API. Make sure your FastAPI server is running in another terminal!"
            )
