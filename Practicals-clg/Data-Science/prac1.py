# Practical no : 01 : Data Frames and Basic Data Pre-processing
# Aim: Read data from CSV and JSON files into a data frame. Perform basic data pre
# processing tasks such as handling missing values and outliers.Manipulate and
# transform data using functions like filtering, sorting, and grouping.

import pandas as pd
import numpy as np

print("Joshua: 48")

# Step 1: Define proper column names
columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

# Step 2: Read CSV with correct column names
df = pd.read_csv(r"C:\Users\Joshua\Downloads\DS-prac\iris.csv", header=None, names=columns)

# Step 3: Basic inspection
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nSummary statistics:")
print(df.describe())
print("\nDataFrame info:")
df.info()
print("\nShape:", df.shape)
print("\nData types:")
print(df.dtypes)

# Step 4: Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values in CSV Data:")
print(missing_values)

# Step 5: Fill missing values with mean (numeric only)
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nFilled Missing Values with Mean (CSV Data):")
print(df_filled.head())

# Step 6: Handling Outliers using Z-score (numeric columns only)
numeric_cols = df_filled.select_dtypes(include=[np.number]).columns
z_scores = np.abs((df_filled[numeric_cols] - df_filled[numeric_cols].mean()) / df_filled[numeric_cols].std())
df_no_outliers = df_filled[(z_scores < 3).all(axis=1)]
print("\nData After Removing Outliers (CSV Data):")
print(df_no_outliers.head())
print("Shape after outlier removal:", df_no_outliers.shape)

# Step 7: Filtering Data (Example: SepalLengthCm > threshold)
threshold_value = 3
df_filtered = df_no_outliers[df_no_outliers['SepalLengthCm'] > threshold_value]
print(f"\nFiltered Data (Rows where 'SepalLengthCm' > {threshold_value}):")
print(df_filtered.head())

# Step 8: Sorting Data (by SepalWidthCm descending)
df_sorted = df_filtered.sort_values(by='SepalWidthCm', ascending=False)
print("\nSorted Data (by 'SepalWidthCm' descending):")
print(df_sorted.head())

# Step 9: Grouping Data (group by SepalLengthCm and aggregate)
df_grouped = df_sorted.groupby('SepalLengthCm').agg({
    'PetalLengthCm': 'mean',  # mean of PetalLengthCm
    'PetalWidthCm': 'sum'     # sum of PetalWidthCm
}).reset_index()
print("\nGrouped Data (Mean and Sum for Each Group):")
print(df_grouped.head())

# Optional: Display filtered data at the end
print("\nFiltered Data Preview:")
print(df_filtered.head())
