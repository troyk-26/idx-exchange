import streamlit as st
import pandas as pd
import joblib
from lightgbm import LGBMRegressor

# Load model
model = joblib.load('lgbm_model.pkl')

st.title('California Home Price Predictor')

st.write('Enter information about a property to estimate its sale price.')

# User inputs
living_area = st.number_input(
    'Living Area (sq ft)',
    min_value=100,
    max_value=20000,
    value=1500
)

beds = st.number_input(
    'Bedrooms',
    min_value=1,
    max_value=20,
    value=3
)

baths = st.number_input(
    'Bathrooms',
    min_value=1,
    max_value=20,
    value=2
)

lot_size = st.number_input(
    'Lot Size (sq ft)',
    min_value=100,
    max_value=100000,
    value=5000
)

if st.button('Predict Price'):

    input_data = pd.DataFrame({
        'LivingArea': [living_area],
        'BedroomsTotal': [beds],
        'BathroomsTotalInteger': [baths],
        'LotSizeSquareFeet': [lot_size]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f'Estimated Price: ${prediction:,.0f}'
    )