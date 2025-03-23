import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load Sample Kubernetes Data (Replace with your dataset)
df = pd.read_csv("k8s_processed_data.csv")  # Assume file has 'timestamp' & 'cpu_usage'
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Normalize Data (LSTM works better with scaled data)
scaler = MinMaxScaler(feature_range=(0,1))
df_scaled = scaler.fit_transform(df[['cpu_usage']])

# Prepare Data for LSTM
def create_sequences(data, seq_length=10):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

seq_length = 10
X, y = create_sequences(df_scaled, seq_length)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))  # Reshape for LSTM

# Build LSTM Model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    tf.keras.layers.LSTM(50),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train Model
model.fit(X, y, epochs=20, batch_size=16)

# Predict Next Values
predicted = model.predict(X)
predicted = scaler.inverse_transform(predicted)

# Plot Results
plt.figure(figsize=(10,5))
plt.plot(df.index[seq_length:], scaler.inverse_transform(df_scaled[seq_length:]), label="Actual CPU Usage")
plt.plot(df.index[seq_length:], predicted, label="Predicted CPU Usage", linestyle="dashed")
plt.legend()
plt.show()
