import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pk1")

st.title("Car Price Prediction App 🚗")

# Mapping dictionaries
name_mapping = {
    'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5,
    'Ford': 6, 'Renault': 7, 'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10,
    'Datsun': 11, 'Jeep': 12, 'Mercedes-Benz': 13, 'Mitsubishi': 14,
    'Audi': 15, 'Volkswagen': 16, 'BMW': 17, 'Nissan': 18, 'MG': 19,
    'Jaguar': 20, 'Daewoo': 21, 'Volvo': 22, 'Kia': 23, 'Fiat': 24,
    'Force': 25, 'Land': 26, 'Ambassador': 27, 'Ashok': 28, 'Isuzu': 29,
    'Opel': 30
}

fuel_mapping = {'Petrol': 2, 'Diesel': 1, 'CNG': 4, 'LPG': 3}

seller_type_mapping = {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3}

transmission_mapping = {'Manual': 1, 'Automatic': 2}

owner_mapping = {'First Owner': 1,'Second Owner': 2,'Third Owner': 3, 'Fourth & Above Owner': 4,'Test Drive Car': 5}

# Inputs
name = st.selectbox("name", list(name_mapping.keys()))
year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
km_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)
fuel = st.selectbox("Fuel Type", list(fuel_mapping.keys()))
seller_type = st.selectbox("Seller Type", list(seller_type_mapping.keys()))
transmission = st.selectbox("Transmission", list(transmission_mapping.keys()))
owner = st.selectbox("Owner", list(owner_mapping.keys()))
mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=18.0)
engine = st.number_input("Engine (CC)", min_value=500, max_value=5000, value=1197)
max_power = st.number_input("Max Power (bhp)", min_value=20.0, max_value=300.0, value=83.0)
seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8, 9, 10])

# Encode categorical values
name_encoded = name_mapping[name]
fuel_encoded = fuel_mapping[fuel]
seller_type_encoded = seller_type_mapping[seller_type]
transmission_encoded = transmission_mapping[transmission]
owner_encoded = owner_mapping[owner]





# Prepare DataFrame
input_data = pd.DataFrame({
    "name": [name_encoded],
    "year": [year],
    "km_driven": [km_driven],
    "fuel": [fuel_encoded],
    "seller_type": [seller_type_encoded],
    "transmission": [transmission_encoded],
    "owner": [owner_encoded],
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
