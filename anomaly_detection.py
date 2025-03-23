import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load Kubernetes Data (Example CSV format)
df = pd.read_csv("k8s_processed_data.csv")  # Assume it has 'timestamp', 'cpu_usage', 'memory_usage'
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Train Isolation Forest
model = IsolationForest(contamination=0.05)  # 5% anomalies expected
df['anomaly'] = model.fit_predict(df[['cpu_usage', 'memory_usage']])

# Plot Results
plt.figure(figsize=(10,5))
plt.scatter(df.index, df['cpu_usage'], c=df['anomaly'], cmap='coolwarm', label="Anomaly Detection")
plt.xlabel("Time")
plt.ylabel("CPU Usage")
plt.legend()
plt.show()
