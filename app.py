# ==========================================
# Car Price Prediction Web Application
# Author: Sariya Khan
# ==========================================

# Import Libraries
import streamlit as st
import pandas as pd
import joblib

# ------------------------------------------
# Configure Web Page
# ------------------------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# ------------------------------------------
# Load Trained Machine Learning Model
# ------------------------------------------
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.error("model.pkl not found. Please run the notebook first and save the model.")
    st.stop()

# ------------------------------------------
# Title
# ------------------------------------------
st.title("🚗 Car Price Prediction System")

st.write(
    """
This application predicts the **selling price of a used car**
using a Machine Learning model trained with Linear Regression.

Enter the car details below and click **Predict Price**.
"""
)

# ------------------------------------------
# Sidebar
# ------------------------------------------
st.sidebar.header("Project Information")

st.sidebar.write("""
### Machine Learning Project

**Algorithm**
- Linear Regression

**Libraries**
- Pandas
- Scikit-learn
- Streamlit

**Developed By**
Sariya Khan
""")

# ------------------------------------------
# User Inputs
# ------------------------------------------

st.subheader("Enter Car Details")

present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)

driven_kms = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=30000,
    step=1000
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

selling_type = st.selectbox(
    "Selling Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0, 1, 2, 3]
)

car_age = st.slider(
    "Car Age (Years)",
    min_value=0,
    max_value=20,
    value=5
)

# ------------------------------------------
# Encoding
# IMPORTANT:
# Use the SAME encoding as used in notebook
# ------------------------------------------

fuel_mapping = {
    "CNG": 0,
    "Diesel": 1,
    "Petrol": 2
}

selling_mapping = {
    "Dealer": 0,
    "Individual": 1
}

transmission_mapping = {
    "Automatic": 0,
    "Manual": 1
}

fuel = fuel_mapping[fuel]
selling_type = selling_mapping[selling_type]
transmission = transmission_mapping[transmission]

# ------------------------------------------
# Prediction
# ------------------------------------------

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Present_Price": [present_price],
        "Driven_kms": [driven_kms],
        "Fuel_Type": [fuel],
        "Selling_type": [selling_type],
        "Transmission": [transmission],
        "Owner": [owner],
        "Car_Age": [car_age]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs"
    )

    st.subheader("Input Summary")

    st.dataframe(input_data)

# ------------------------------------------
# Footer
# ------------------------------------------

st.markdown("---")

st.caption(
    "Car Price Prediction using Machine Learning | Developed by Sariya Khan"
)