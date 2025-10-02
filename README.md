House Price Prediction
Project Overview

This project is a machine learning model that predicts the price of a house based on key housing features. The model is built using Python and the Linear Regression algorithm from scikit-learn. It uses feature engineering to improve prediction accuracy.

The model predicts house prices in a given region using features such as the age of the house, number of bedrooms per room, and population per household.

Dataset

The dataset used is the California Housing dataset (housing.csv).

It contains the following key columns:

total_rooms: Total number of rooms in the block

total_bedrooms: Total number of bedrooms

population: Total population of the block

households: Number of households

housing_median_age: Median age of houses in the block

median_house_value: Target variable (house price)

ocean_proximity: Categorical feature (not used in this simple version)

Features Used

The following features are used after feature engineering:

housing_median_age – Age of the house.

bedrooms_per_room – Calculated as total_bedrooms / total_rooms.

people – Calculated as population / households.

These engineered features help the model better understand the relationships between the raw data and the house price.

Model

Algorithm: Linear Regression (from scikit-learn)

Training/Test Split: 80% training, 20% testing

Evaluation Metric: Mean Squared Error (MSE)

How to Run

Install the required Python libraries:

pip install pandas scikit-learn


Place the housing.csv dataset in the specified path.

Run the Python script:

python house_price_prediction.py


Enter the requested user inputs:

Total rooms

Total bedrooms

Age of the house

Population

Number of households

The script will output the predicted house price.
