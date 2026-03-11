# Practical no : 01 : Data Frames and Basic
# Data Pre-processing

# Aim: Read data from CSV and JSON files
# into a data frame. Perform basic data pre
# processing tasks such as handling missing
# values and outliers.Manipulate and
# transform data using functions like
# filtering, sorting, and grouping

import pandas as pd 
import numpy as np

columns = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm',
    'Species'
]

# step 1: Reading a CSV file into a DataFrame 
df = pd.read_csv(r"Iris.csv", names=columns)

# step 2: displays the first 5 rows of the dataset (Basic Data Exploration)
print(df.head())
# displays the last 5 rows of the dataset
print(df.tail())

# displays summary of the dataset such as mean, count, percentage
print(df.describe())
# displays information about the dataset
print(df.info())

# displays dimensions of the dataset
print(df.shape)
# displays datatypes
print(df.dtypes)
# displays column names 
print(df.columns)

# Step 3: Checking for Missing Values
# Checking for missing values in each column of the CSV DataFrame
missing_values = df.isnull().sum()

print("\nMissing values in CSV data: ")
print(missing_values)

df = df.drop(columns=['Species'])

# Step 4: Handling Missing Values
# We will fill missing values in columns with the mean of the column
fill = df.fillna(df.mean())
print("\nFilled Missing Values with Mean (CSV Data): ")
print(df.head())

# Step 5: Handling Outliers
# Here we will calculate Z-scores and remove rows where Z-score is greater than 3
z_scores = np.abs((fill - fill.mean()) / fill.std())
print(z_scores)

 # Remove rows where any Z-score is greater than 3 (outliers)
do = fill[(z_scores < 3).all(axis = 1)]
print("\nData after removing outliers (CSV Data): ")
print(do.head())

 # Step 6: Filtering Data (Example: Select rows where a column value is greater than 3
threshold_value = 3
filter = do[do['SepalLengthCm'] > threshold_value]
print(f"\nFiltered Data (Rows with column_name > {threshold_value}): ")
print(filter)

 # Step 7: Sorting Data (Sorting by a column in descending order)
df_sorted = filter.sort_values(by='SepalWidthCm', ascending=False)
print(df_sorted.head())

 # Step 8: Grouping Data
df_grouped = df_sorted.groupby('SepalLengthCm').agg({'PetalLengthCm': 'mean',
                                                    'PetalWidthCm': 'sum'}).reset_index()
print("]nGrouped Data (Mean and Sum for Each Group): ")
print(df_grouped.head())