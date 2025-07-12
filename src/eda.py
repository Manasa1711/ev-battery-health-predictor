import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/simulated_ev_data.csv")

# Battery Health Distribution
sns.histplot(df["battery_health"], kde=True)
plt.title("Battery Health Distribution")
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
