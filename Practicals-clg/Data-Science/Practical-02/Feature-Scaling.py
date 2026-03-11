# Practical No 02: Feature Scaling and
# Dummification

# Part I: Apply feature-scaling techniques
# like standardization and normalization to
# numerical features

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv(r"wine.csv")
print(df)

df1 = pd.read_csv(r"wine.csv", usecols=[0, 1, 2], skiprows=1)
df1.columns = ['classlabel', 'Alcohol', 'Malic Acid']
print("Original DataFrame: ")
print(df1)

scaling = MinMaxScaler()
scaled_value = scaling.fit_transform(df1[['Alcohol', 'Malic Acid']])
df1[['Alcohol', 'Malic Acid']] = scaled_value
print("\n Dataframe after MinMax scaling")
print(df1)


scaling = StandardScaler()
scaled_standardvalue = scaling.fit_transform(df1[['Alcohol','Malic Acid']])
# Convert scaled values into a DataFrame
scaled_df = pd.DataFrame(
    scaled_standardvalue,
    columns=['Alcohol', 'Malic Acid']
)
print("\n Dataframe after standard scaling")
print(scaled_df)

