import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Define the categories based on provided arrays
car_names = ['Ambassador Classic Nova Diesel', 'Audi A3 35 TDI', 'Audi A4 1.8 TFSI', 
             'Volvo XC60 D5', 'Volvo XC60 D5 Inscription', 'Volvo XC90 2007-2015 D5']
locations = ['Ahmedabad', 'Bangalore', 'Chennai', 'Coimbatore', 'Delhi', 'Hyderabad',
             'Jaipur', 'Kochi', 'Kolkata', 'Mumbai', 'Pune']
fuel_types = ['CNG', 'Diesel', 'LPG', 'Petrol']
transmissions = ['Automatic', 'Manual']
owner_types = ['First', 'Fourth', 'Second', 'Third']
companies = ['Ambassador', 'Audi', 'BMW', 'Bentley', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 
             'Ford', 'Honda', 'Hyundai', 'ISUZU', 'Isuzu', 'Jaguar', 'Jeep', 'Lamborghini', 
             'Land', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 
             'Porsche', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #F8F9FA;
    }
    .css-1d391kg {
        padding-top: 2rem;
    }
    .block-container {
        padding: 2rem 2rem;
    }
    h1 {
        color: #2C3E50;
    }
    .sidebar .sidebar-content {
        background-color: #ECEFF1;
    }
    </style>
    """, unsafe_allow_html=True
)

# Application Title and Description
st.title("🚗 Car Price Prediction")
st.markdown("""
Welcome to the **Car Price Prediction App**! 
This application uses a pre-trained machine learning model to estimate the price of used cars based on several features such as the car's name, location, year of manufacture, and more.

Please enter the car details below to get the predicted price.
""")

# Divider
st.markdown("---")

# Define the input form with headings and instructions
st.header("🔧 Car Details Input")

def user_input_features():
    st.subheader("Basic Information")
    name = st.selectbox('Car Name', car_names, help="Select the model of the car.")
    location = st.selectbox('Location', locations, help="Select the city where the car is being sold.")
    year = st.number_input('Year', min_value=1990, max_value=2024, value=2011, help="Enter the year of manufacture.")
    kilometers_driven = st.number_input('Kilometers Driven', min_value=0, max_value=1000000, value=46000, help="Enter the total kilometers the car has been driven.")

    st.subheader("Technical Specifications")
    fuel_type = st.selectbox('Fuel Type', fuel_types, help="Select the type of fuel the car uses.")
    transmission = st.selectbox('Transmission', transmissions, help="Select the type of transmission.")
    owner_type = st.selectbox('Owner Type', owner_types, help="Select the type of ownership.")

    st.subheader("Performance Metrics")
    mileage = st.number_input('Mileage (km/l)', min_value=0.0, max_value=100.0, value=18.20, help="Enter the car's mileage.")
    engine = st.number_input('Engine (CC)', min_value=500, max_value=10000, value=1199, help="Enter the engine capacity in CC.")
    power = st.number_input('Power (BHP)', min_value=10.0, max_value=1000.0, value=88.70, help="Enter the power of the car in BHP.")
    company_name = st.selectbox('Company Name', companies, help="Select the company that manufactures the car.")
    
    # Create a dictionary with user inputs
    data = {
        'Name': name,
        'Location': location,
        'Year': year,
        'Kilometers_Driven': kilometers_driven,
        'Fuel_Type': fuel_type,
        'Transmission': transmission,
        'Owner_Type': owner_type,
        'Mileage': mileage,
        'Engine': engine,
        'Power': power,
        'Company_Name': company_name
    }
    
    features = pd.DataFrame([data])
    return features

# Get user input
input_df = user_input_features()

# Divider
st.markdown("---")

# Prediction Section
st.header("🔍 Prediction")

if st.button('Predict'):
    prediction = model.predict(input_df)
    st.success(f"The estimated price for the car is: ₹{prediction[0]:.2f} lac")

# Footer with additional information
st.markdown("""
---
*This app is developed as a demonstration of car price prediction using machine learning. The model is trained on historical data and the results are only estimations.*
""")
