import streamlit as st
import pandas as pd
import joblib

# ===============================
# Load model and scaler
# ===============================
model = joblib.load("weather_model_multi.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Weather Prediction", page_icon="🌤")

st.title("🌤 Daily Temperature Prediction")
st.write("Predict temperature using sunlight hours and humidity level")

# ===============================
# User Inputs
# ===============================
hours = st.slider("Hours of Sunlight", 0.0, 24.0, 8.0)
humidity = st.slider("Humidity Level (%)", 0, 100, 70)

# ===============================
# Prediction
# ===============================
if st.button("Predict Temperature"):
    # Convert input to DataFrame (same as training)
    input_df = pd.DataFrame(
        [[hours, humidity]],
        columns=['hours_sunlight', 'humidity_level']
    )

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(f"🌡 Predicted Temperature: {prediction[0]:.2f} °C")