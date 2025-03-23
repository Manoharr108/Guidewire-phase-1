import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points
num_samples = 10000

# Generate timestamps
timestamps = pd.date_range(start="2025-01-01", periods=num_samples, freq="5T")  # Every 5 minutes

# Simulate CPU Usage (Normal range: 20-80%, but spikes occur)
cpu_usage = np.random.normal(50, 10, num_samples)  # Mean 50%, Std Dev 10
cpu_usage[cpu_usage > 90] = 95  # Cap CPU at 95%

# Simulate Memory Usage (Normal range: 30-90%, with occasional spikes)
memory_usage = np.random.normal(60, 15, num_samples)
memory_usage[memory_usage > 95] = 99  # Cap memory at 99%

# Simulate Disk Usage (Slowly increasing over time)
disk_usage = np.linspace(20, 80, num_samples) + np.random.normal(0, 5, num_samples)

# Simulate Network I/O (High fluctuation)
network_io = np.random.randint(100, 1000, num_samples)

# Simulate Pod Status (Most are Running, some fail)
pod_status = np.random.choice(["Running", "Failed", "Pending"], num_samples, p=[0.92, 0.05, 0.03])

# Combine all data into a DataFrame
df = pd.DataFrame({
    "timestamp": timestamps,
    "cpu_usage": np.clip(cpu_usage, 0, 100),  # Ensure values stay in range
    "memory_usage": np.clip(memory_usage, 0, 100),
    "disk_usage": np.clip(disk_usage, 0, 100),
    "network_io": network_io,
    "pod_status": pod_status
})

# Save dataset to CSV
df.to_csv("k8s_synthetic_data.csv", index=False)

print("Data generation complete! Saved as k8s_synthetic_data.csv")
