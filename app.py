import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("Car Price Prediction App 🚗")
st.write("Fill in the details of the car below to predict its selling price.")

# Input form
brand = st.selectbox("Brand", ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'MG',
       'Jaguar', 'Daewoo', 'Volvo', 'Kia', 'Fiat', 'Force', 'Land',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'])  # Add all brands
year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
km_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=18.0)
engine = st.number_input("Engine (CC)", min_value=500, max_value=5000, value=1197)
max_power = st.number_input("Max Power (bhp)", min_value=20.0, max_value=300.0, value=83.0)
seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8, 9, 10])

# Convert inputs into DataFrame (format must match training data)
input_data = pd.DataFrame({
    "brand": [brand],
    "year": [year],
    "km_driven": [km_driven],
    "fuel": [fuel],
    "seller_type": [seller_type],
    "transmission": [transmission],
    "owner": [owner],
    "mileage": [mileage],
    "engine": [engine],
    "max_power": [max_power],
    "seats": [seats]
})

# Predict button
if st.button("Predict Selling Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Estimated Selling Price: ₹{int(prediction[0]):,}")
    except Exception as e:
        st.error(f"Error: {e}")
