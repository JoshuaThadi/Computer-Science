# Practical No 02: Feature Scaling and Dummification
# Part I: Apply feature-scaling techniques like standardization and normalization to
# numerical features

print("Joshua: 48")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 1: Read dataset
df = pd.read_csv(r"C:\Users\Joshua\Downloads\DS-prac\wine.csv")

# Step 2: Select required columns (skip header row)
df1 = pd.read_csv(
    r"C:\Users\Joshua\Downloads\DS-prac\wine.csv",
    usecols=[0, 1, 2],
    skiprows=1,
    header=None
)

# Step 3: Assign column names
df1.columns = ['ClassLabel', 'Alcohol', 'Malic_Acid']

print("\nOriginal DataFrame:")
print(df1.head())

# -----------------------------
# Min-Max Normalization
# -----------------------------
minmax_scaler = MinMaxScaler()
df1[['Alcohol', 'Malic_Acid']] = minmax_scaler.fit_transform(
    df1[['Alcohol', 'Malic_Acid']]
)

print("\nAfter Min-Max Scaling:")
print(df1.head())

# -----------------------------
# Standardization (Z-score)
# -----------------------------
standard_scaler = StandardScaler()
df1[['Alcohol', 'Malic_Acid']] = standard_scaler.fit_transform(
    df1[['Alcohol', 'Malic_Acid']]
)

print("\nAfter Standard Scaling:")
print(df1.head())
