# Aim: Logistic Regression and Decision Tree
# Part I: Build a logistic regression model to
# predict a binary outcome. Evaluate the
# model's performance using classification
# metrics (e.g., accuracy, precision, recall).

import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

columns = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm',
    'Species'
]

df = pd.read_csv(r"Iris.csv", names=columns)
print(df)

df1 = df[df['Species'] != 2]
print(df1)

df = df[df['Species'] != 2]
X = df.drop('Species', axis=1)
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
logistic_model = LogisticRegression()
print(logistic_model.fit(X_train, y_train))

y_pred_logistic = logistic_model.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred_logistic))
print("\nClassification Report")
print(classification_report(y_test, y_pred_logistic))
