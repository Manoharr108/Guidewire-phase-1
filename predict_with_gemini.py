import google.generativeai as genai
import pandas as pd

# Load API Key
genai.configure(api_key="AIzaSyCezzX-vgWa0ZQ8_gr5HrbVpP_CERW9hNQ")

# Load Processed Data
df = pd.read_csv("k8s_processed_data.csv")

# Convert data to JSON for Gemini
data_samples = df.head(10).to_dict(orient="records")  # Send only a few samples

# Define the prompt
prompt = f"""
I have Kubernetes cluster metrics, including CPU, memory, disk, network usage, and pod status.
Here is the data:

{data_samples}

Based on this data, predict if there will be any issues such as pod failures, resource exhaustion, or network problems.
Provide a detailed explanation.
"""

# Get Gemini's response
model = genai.GenerativeModel("gemini-1.5-pro-latest")
response = model.generate_content(prompt)

# Print the prediction
print("\nGemini Prediction:")
print(response.text)
