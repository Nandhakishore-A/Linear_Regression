🌤️ Linear Regression – Weather Temperature Predictor

A Machine Learning web application that predicts daily temperature (°C) based on environmental factors such as hours of sunlight and humidity level.
The model is built using Linear Regression and deployed using Streamlit.

🔗 Live Demo:
👉 https://linearregression00.streamlit.app/

🔗 Repository:
👉 https://github.com/Nandhakishore-A/Linear_Regression

📌 About the Project

This project demonstrates the use of Linear Regression, a supervised machine learning algorithm, to predict a continuous numerical value.

The model is trained on historical weather data and learns the linear relationship between environmental features and temperature.
Users can enter real-time values through a Streamlit web interface, and the trained model instantly predicts the expected daily temperature.

This project is optimized for deployment on Streamlit Cloud and is suitable for beginners learning regression concepts.

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

Machine Learning: Scikit-Learn, Joblib

Algorithm: Linear Regression

Data Processing: NumPy, Pandas

Deployment: Streamlit Cloud

▶️ How to Run Locally

Follow these steps to run the project on your local system:

1️⃣ Clone the Repository
git clone https://github.com/Nandhakishore-A/Linear_Regression.git
cd Linear_Regression

2️⃣ Install Dependencies

Make sure Python is installed, then run:

pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

4️⃣ Open in Browser

Streamlit will automatically open the app in your browser.
If not, visit:

http://localhost:8501

🤖 Model Details

Algorithm: Linear Regression

Library Used: Scikit-Learn

Learning Type: Supervised Learning (Regression)

Model File: weather_model_multi.pkl

Feature Scaling: StandardScaler (scaler.pkl)

🔢 Input Features

The model takes the following input features:

Hours of Sunlight

Humidity Level (%)

These features are scaled before prediction to improve model accuracy.

📤 Output

Predicted Daily Temperature (°C)

Result is displayed instantly on the Streamlit web interface

📂 Project Structure
Linear_Regression/
│
├── app.py                     # Streamlit application
├── train_weather_model.py     # Model training script
├── weather_model_multi.pkl    # Trained Linear Regression model
├── scaler.pkl                 # Feature scaler
├── requirements.txt           # Project dependencies
└── DATA_SETS/
    └── weather_data.csv       # Dataset

🌐 Application Workflow

User enters environmental values (sunlight, humidity)

Input data is scaled using the saved scaler

Trained Linear Regression model is loaded

Temperature prediction is generated

Result is displayed on the Streamlit UI

🤝 Contributing

Contributions are welcome 🚀
You can:

Improve the UI design

Add evaluation metrics (R² score, MAE, MSE)

Add data visualizations

Improve model performance with more features

Fork the repository and submit a pull request.

👨‍💻 Author

Nandhakishore A
Machine Learning | Data Science | AI Enthusiast 🔥
