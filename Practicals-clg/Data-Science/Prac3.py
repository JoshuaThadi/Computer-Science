# Practical No: 03 - Regression and Its Types
# Aim: Implement Simple Linear Regression and interpret results

print("Joshua 48")

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load California Housing dataset
housing = fetch_california_housing()

# Convert to DataFrame
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df['PRICE'] = housing.target

# Basic exploration
print(housing_df.head())
print(housing_df.tail())
print(housing_df.shape)
print(housing_df.size)
print(housing_df.describe())
print(housing_df.info())
print(housing_df.dtypes)

# Feature (Independent variable) and Target (Dependent variable)
X = housing_df[['AveRooms']]   # Simple Linear Regression
y = housing_df['PRICE']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Results
print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
