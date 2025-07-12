import pandas as pd
import numpy as np
import os

def generate_ev_data(num_vehicles=100, num_days=30):
    data = []
    for v_id in range(1, num_vehicles + 1):
        health = 100
        for day in range(1, num_days + 1):
            temp = np.random.normal(30, 5)
            cycles = np.random.randint(1, 4)
            soc = np.random.randint(20, 100)
            distance = np.random.uniform(30, 150)
            health -= np.random.uniform(0.05, 0.3)
            health = max(health, 70)
            data.append([v_id, day, temp, cycles, soc, distance, round(health, 2)])
    df = pd.DataFrame(data, columns=["vehicle_id", "day", "temperature_c", "charge_cycles", "state_of_charge", "distance_km", "battery_health"])
    
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/simulated_ev_data.csv", index=False)
    print("✅ Data saved to data/simulated_ev_data.csv")

if __name__ == "__main__":
    generate_ev_data()
