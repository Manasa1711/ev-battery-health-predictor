import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/simulated_ev_data.csv")

# Train model
X = df[["temperature_c", "charge_cycles", "state_of_charge", "distance_km"]]
y = df["battery_health"]
model = LinearRegression()
model.fit(X, y)

# App Interface
st.title("🔋 EV Battery Health Predictor")
st.write("Predict EV battery health based on simple vehicle telemetry.")

temperature = st.slider("Temperature (°C)", 15, 45, 30)
cycles = st.slider("Charge Cycles Today", 1, 5, 2)
soc = st.slider("State of Charge (%)", 10, 100, 60)
distance = st.slider("Distance Travelled (km)", 10, 200, 100)

input_df = pd.DataFrame([[temperature, cycles, soc, distance]],
                        columns=["temperature_c", "charge_cycles", "state_of_charge", "distance_km"])

prediction = model.predict(input_df)[0]

st.success(f"🔋 Predicted Battery Health: **{round(prediction, 2)}%**")
