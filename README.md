# Linear_Regression

🌤️ Weather Temperature Predictor

A Machine Learning web application that predicts daily temperature based on features like hours of sunlight and humidity level. The model is built using Linear Regression and deployed using Streamlit.

Live Demo:
Click here to view the Live App

About the Project:
This project uses a Linear Regression model trained on weather data. The goal is to predict the daily temperature based on user-provided environmental inputs.

The application is built using Streamlit (Python) and provides a simple, interactive interface for prediction. The project is optimized for deployment on Streamlit Cloud.

Tech Stack:
Frontend: Streamlit
Backend: Python
Machine Learning: Scikit-Learn, Joblib
Deployment: Streamlit Cloud

Project Structure.
├── app.py                     # Streamlit application
├── train_weather_model.py     # Script to train the model
├── weather_model_multi.pkl    # Trained Machine Learning model
├── scaler.pkl                 # Feature scaler
├── requirements.txt           # List of dependencies
└── DATA_SETS/
    └── weather_data.csv       # Dataset
    
How to Run Locally
If you want to run this project on your own computer, follow these steps:

1.Clone the Repository git clone 
https://github.com/your-username/your-repo-name.git
cd your-repo-name

2.Install Dependencies
Make sure you have Python installed, then run:
pip install -r requirements.txt

3.Run the App
streamlit run app.py

Model Details
The model was trained using Scikit-Learn’s LinearRegression.
It takes the following inputs to make a prediction:

* Hours of Sunlight
* Humidity Level (%)
Output:
* Daily Temperature (°C)

Contributing:
Feel free to fork this repository and submit pull requests if you want to improve the model or the UI.
