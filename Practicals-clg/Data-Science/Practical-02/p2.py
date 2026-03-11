# Practical No 02: Feature Scaling and
# Dummification

# Part I: Apply feature-scaling techniques
# like standardization and normalization to
# numerical features

import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScalar

df = pd.read_csv(r"wine.csv")
print(df)