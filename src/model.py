import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("data/simulated_ev_data.csv")

X = df[["temperature_c", "charge_cycles", "state_of_charge", "distance_km"]]
y = df["battery_health"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

rmse = mean_squared_error(y_test, model.predict(X_test), squared=False)
print(f"✅ Model trained. RMSE: {rmse:.2f}")
