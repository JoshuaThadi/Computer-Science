# Part II: Construct a decision tree modeland interpret the decision rules for classification.

# Part II: Decision Tree Classification
print("\nJoshua 48")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load CSV (same as Part I)
df = pd.read_csv(r"C:\Users\Joshua\Downloads\DS-prac\Iris.csv", header=None)
df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

# Keep only 2 classes for binary classification
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

# Decision Tree model
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Predictions
y_pred_tree = tree_model.predict(X_test)

# Evaluation
print("\n--- Decision Tree ---")
print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred_tree))
