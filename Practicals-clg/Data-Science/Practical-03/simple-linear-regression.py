# Practical No: 03 - Regression and Its Types
# Aim : To Implement simple linear
# regression using a dataset.Explore and
# interpret the regression model coefficients
# and goodness-of-fit measures.

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_excel(r"fetch_california_housing.xlsx")
print("Dataset Preview:")

print(df.head())
print(df.tail())

print(df.shape)
print(df.size)

print(df.describe())
print(df.info())
print(df.dtypes)

housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(housing_df.head())

housing_df['PRICE'] = housing.target
X = housing_df[['AveRooms']]
y = housing_df[['PRICE']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
print(model.fit(X_train, y_train))

mse = mean_squared_error(y_test, model.predict(X_test))
r2 = r2_score(y_test, model.predict(X_test))

print("Mean Squared Error: ", mse)
print("R-squared: ", r2)
print("Intercept: ", model.intercept_)
print("Co-efficient:", model.coef_)