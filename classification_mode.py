import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load Kubernetes Data
df = pd.read_csv("k8s_processed_data.csv")
df['label'] = pd.cut(df['cpu_usage'], bins=[0, 50, 75, 100], labels=[0, 1, 2])  # 0=Normal, 1=Warning, 2=Critical

# Prepare Data
X = df[['cpu_usage', 'memory_usage', 'network_io']]
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
