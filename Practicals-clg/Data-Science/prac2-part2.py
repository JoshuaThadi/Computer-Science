# Practical No 02
# Part II: Perform feature dummification to convert categorical variables
# into numerical representations

print("Joshua: 48")

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Define correct column names (CSV has NO headers)
columns = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm',
    'Species'
]

# Step 2: Read CSV with assigned column names
iris = pd.read_csv(
    r"C:\Users\Joshua\Downloads\DS-prac\iris.csv",
    header=None,
    names=columns
)

# Step 3: Display original dataset
print("\nOriginal Dataset:")
print(iris.head())

# Step 4: Apply Label Encoding on categorical column
le = LabelEncoder()
iris['Species_Code'] = le.fit_transform(iris['Species'])

# Step 5: Display encoded dataset
print("\nDataset After Label Encoding:")
print(iris.head())

# Step 6: Show encoding mapping (important for exam/viva)
print("\nEncoding Mapping:")
for cls, code in zip(le.classes_, le.transform(le.classes_)):
    print(f"{cls} -> {code}")
