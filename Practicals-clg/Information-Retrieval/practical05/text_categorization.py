# text_categorization.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the CSV file (make sure file name has .csv)
df = pd.read_csv("/content/Dataset.csv")

# Combine the text columns
data = df["covid"].astype(str) + " " + df["fever"].astype(str)

X = data                      # Text features
y = df["flu"]                # Target labels

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Bag-of-Words conversion
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train Naive Bayes model
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)

# Load new dataset for prediction
data1 = pd.read_csv("/content/Dataset.csv")

# Combine columns similar to training
new_data = data1["covid"].astype(str) + " " + data1["fever"].astype(str)
new_data_counts = vectorizer.transform(new_data)

# Make predictions
predictions = classifier.predict(new_data_counts)

print("\nPredictions for new data:")
print(predictions)

# Evaluate model
accuracy = accuracy_score(y_test, classifier.predict(X_test_counts))
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, classifier.predict(X_test_counts)))

# Add predictions to DataFrame
data1["flu_prediction"] = predictions

# Save output
output_path = "/content/Output.csv"
data1.to_csv(output_path, index=False)

print(f"\nPredictions saved to: {output_path}")
print("\nPerformed by Joshua Thadi 48")
