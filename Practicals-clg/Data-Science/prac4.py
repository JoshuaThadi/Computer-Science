# Practical: Logistic Regression
# Aim: Predict a binary outcome and evaluate classification metrics

# Part I: Logistic Regression (Binary Classification)
print("Joshua 48")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# Load CSV (no headers)
df = pd.read_csv(r"C:\Users\Joshua\Downloads\DS-prac\Iris.csv", header=None)

# Assign correct column names (5 columns)
df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

# Keep only 2 classes (remove Iris-virginica)
df = df[df['Species'] != 'Iris-virginica']

# Features & target
X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

# Encode target
le = LabelEncoder()
y = le.fit_transform(y)  # 0 = setosa, 1 = versicolor

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Logistic Regression
log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train)

# Predictions
y_pred = log_model.predict(X_test)

# Evaluation
print("\n--- Logistic Regression ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
