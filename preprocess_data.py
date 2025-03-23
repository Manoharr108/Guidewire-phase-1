import pandas as pd

# Load dataset
df = pd.read_csv("k8s_synthetic_data.csv")

# Convert timestamp to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Convert pod status to numeric values (Running=0, Failed=1, Pending=2)
df["pod_status"] = df["pod_status"].map({"Running": 0, "Failed": 1, "Pending": 2})

# Select relevant features
features = ["cpu_usage", "memory_usage", "disk_usage", "network_io", "pod_status"]

# Prepare data for Gemini (Convert to JSON format)
data_samples = df[features].to_dict(orient="records")

# Save processed data
df.to_csv("k8s_processed_data.csv", index=False)

print("Data preprocessing complete! Ready for Gemini API.")
