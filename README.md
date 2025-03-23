# **AI/ML Model for Predicting Kubernetes Issues 🚀**  

## **Overview**  
Kubernetes clusters can experience failures such as pod crashes, resource bottlenecks, and network issues. This project aims to build an AI/ML model capable of predicting these failures before they occur by analyzing historical and real-time cluster metrics.  

## **Features**  
✔ Predicts **node or pod failures**  
✔ Detects **resource exhaustion (CPU, memory, disk)**  
✔ Identifies **network or connectivity issues**  
✔ Analyzes **service disruptions using logs and events**  
✔ Supports **anomaly detection & time-series analysis**  

## **Project Structure**  
```
📂 AI-ML-K8s-Predictor  
 ├── 📁 data                  # Dataset (simulated or collected)  
 ├── 📁 models                # Trained models  
 ├── 📁 scripts               # Data processing and training scripts  
 ├── train_model.py           # Model training script  
 ├── predict_with_gemini.py   # Prediction script using Gemini API  
 ├── requirements.txt         # Python dependencies  
 ├── README.md                # Project documentation  
```

## **Installation & Setup**  

### **1️⃣ Install Dependencies**  
Make sure you have **Python 3.10** installed. Then, install dependencies:  

```bash
pip install -r requirements.txt
```

### **2️⃣ Train the Model**  
Run the following command to train the model:  

```bash
python train_model.py
```

### **3️⃣ Make Predictions**  
Use the trained model to predict Kubernetes issues:  

```bash
python predict_with_gemini.py
```

---

## **Model Training Approach**  

This project uses a combination of **AI/ML techniques** for accurate predictions.  

### **📌 Time-Series Models**  
- **LSTM (Long Short-Term Memory)**: Used for sequential data and trend analysis.  
- **ARIMA (AutoRegressive Integrated Moving Average)**: Effective for forecasting Kubernetes resource usage.  
- **Prophet (by Facebook/Meta)**: Used for handling seasonality and long-term trend predictions.  

### **📌 Anomaly Detection Models**  
- **Isolation Forest**: Detects outliers in resource usage data.  
- **Autoencoder Neural Networks**: Learns normal Kubernetes behavior and flags deviations.  

### **📌 Supervised Learning (Classification)**  
- **Labeled Kubernetes issues into categories:**  
  - **Normal**  
  - **Warning**  
  - **Critical**  

---

## **Gemini API Integration**  

This project integrates the **Google Gemini API** for enhanced AI-driven predictions.

### **1️⃣ Setup API Key**  
Ensure you have the Gemini API key configured in your environment:  

```bash
export GEMINI_API_KEY="your_api_key_here"
```
Or set it in Windows (PowerShell):  

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### **2️⃣ Modify the Prediction Script**  
The **`predict_with_gemini.py`** script sends Kubernetes metrics to the Gemini model for AI-driven predictions.

---

## **Dataset Generation**  

If you don't have real Kubernetes cluster data, you can generate synthetic data using:  

```bash
python generate_k8s_data.py
```

This script simulates key metrics like CPU usage, memory usage, disk space, and network I/O.

---

## **Results & Observations**  

After running predictions, the model provides:  
✅ **Alerts for resource bottlenecks**  
✅ **Early warning on potential failures**  
✅ **Insights into Kubernetes cluster health**  

---

## **Future Enhancements**  
🔹 Improve accuracy with more real-world Kubernetes logs.  
🔹 Implement real-time anomaly detection.  
🔹 Extend integration with Kubernetes monitoring tools (Prometheus, Grafana).  

---

## **Contributing**  
Want to contribute? Feel free to submit a PR or raise an issue!  

---

## **License**  
MIT License 📜

---

## **Author**  
👨‍💻 Manohar R
📧 manohar2004gr@gmail.com
📌 GitHub: [YourGitHub](https://github.com/manoharr108)  
