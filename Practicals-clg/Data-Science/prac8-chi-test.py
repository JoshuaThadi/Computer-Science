# Hypothesis Testing - Conduct a hypothesis test using appropriate statistical tests (e.g., t-test, chi-square test)

import pandas as pd
import seaborn as sb
import warnings
from scipy import stats

print("Joshua 48")

warnings.filterwarnings('ignore')

# Load dataset
df = sb.load_dataset('mpg')
print(df)

# Describe columns
print(df['horsepower'].describe())
print(df['model_year'].describe())

# Create bins for horsepower
bins = [0, 75, 150, 240]
df['horsepower_new'] = pd.cut(
    df['horsepower'],
    bins=bins,
    labels=['l', 'm', 'h']
)

c = df['horsepower_new']
print(c)

# Create bins for model year
ybins = [69, 72, 74, 84]
label = ['t1', 't2', 't3']

df['modelyear_new'] = pd.cut(
    df['model_year'],
    bins=ybins,
    labels=label
)

newyear = df['modelyear_new']
print(newyear)

# Create contingency table
df_chi = pd.crosstab(df['horsepower_new'], df['modelyear_new'])
print(df_chi)

# Chi-square test
print(stats.chi2_contingency(df_chi))
