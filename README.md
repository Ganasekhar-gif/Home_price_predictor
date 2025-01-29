# Home_price_predictor
A machine learning model built to estimate house prices based on various features like location, square footage, number of bedrooms, and bathrooms. The project involves data preprocessing, feature engineering, model training, creating a Flask API for requests, and a frontend website to interact with the API for real-time predictions.

# Table of Contents            
Project Overview              
Technologies Used                
Dataset
Project Steps
1. Data Cleaning
2. Feature Engineering
3. Handling Outliers
4. Model Building and Training
5. Flask API Server
6. Frontend Web Application
How to Run the Project
Conclusion

# Project Overview
This project leverages machine learning techniques to predict the estimated price of a house based on features such as its location, size (in square feet), the number of bedrooms (BHK), and the number of bathrooms. The model is deployed through a Flask server and can be accessed via a simple web interface where users can input their home details and get an estimated price.

# Technologies Used
Python: Used for data preprocessing, machine learning, and Flask API server.
Flask: Python web framework used to create a backend API for predictions.
Machine Learning Libraries: scikit-learn for model building, pandas and numpy for data manipulation, matplotlib and seaborn for visualization.
HTML/CSS/JavaScript: Frontend technologies for creating a user-friendly interface.
Jupyter Notebook: For initial analysis and model training.

# Dataset
The dataset consists of the following columns:
Total_Sqft: The total area of the house in square feet.
Location: The city or neighborhood where the house is located.
BHK: Number of bedrooms in the house.
Bath: Number of bathrooms in the house.
Price: The actual price of the house (target variable).
The dataset can be found in the dataset folder or sourced from relevant real estate APIs.

 Project Steps
1. Data Cleaning
The first step involves cleaning the dataset by removing or handling missing values, incorrect entries, and duplicates. This ensures that the dataset is ready for analysis and modeling.

Missing values are either filled with mean/median values or dropped depending on the feature's importance.
Invalid rows or inconsistent entries are removed.
2. Feature Engineering
We perform feature engineering to create additional useful features or modify existing ones for better predictive power.

Convert categorical variables like location into numerical values using one-hot encoding or label encoding.
Normalize or scale continuous features such as total_sqft to improve model performance.
3. Handling Outliers
Outliers can skew predictions and distort model accuracy. Therefore, we identify and remove or cap outliers in critical numerical features, particularly in the total_sqft and price columns.

We use statistical methods like the Z-score or Interquartile Range (IQR) to detect and remove outliers.
4. Model Building and Training
We use regression models to predict the price based on input features. The steps for model building are:

Split the data into training and testing sets (80/20 split).
Train the model using algorithms like Linear Regression, Random Forest Regressor, or XGBoost.
Evaluate the model’s performance using metrics such as RMSE (Root Mean Squared Error) and R² score.
The best-performing model is selected based on the evaluation metrics and saved for use in predictions.

5. Flask API Server
We create a Flask-based API to serve predictions. The API has two main endpoints:

/get_location_names: Returns a list of available locations for the user to select.
/predict_home_price: Accepts a POST request with parameters such as total_sqft, location, bhk, and bath and returns the estimated price of the house.

6. Frontend Web Application
A simple HTML website is created with the following features:

Form for input: Users can input values such as location, square footage, number of bedrooms, and bathrooms.
Prediction Button: A button that triggers the prediction process by calling the Flask API.
Result Display: Once the prediction is made, the result (estimated price) is displayed on the page.

# How to Run the Project
1. Clone the repository:
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
2. Install the required dependencies:
   pip install -r requirements.txt
3. Start the Flask API server:
   python app.py
4. Open the website in a browser:
Navigate to http://127.0.0.1:5000 to access the home price prediction web interface.

5. Input the house details and click "Predict" to get the estimated price.

# Conclusion
This project demonstrates a complete end-to-end solution for predicting house prices using machine learning, Flask, and a web-based frontend. It involves data cleaning, feature engineering, model training, API deployment, and user interface development. The system provides an interactive platform for users to estimate home prices in real-time by leveraging the trained model.
