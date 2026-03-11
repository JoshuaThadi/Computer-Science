# Part II : Perform feature Dummification to
# convert categorical variables into
# numerical representations.

import pandas as pd 
from sklearn.preprocessing import LabelEncoder

columns = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm',
    'Species'
]

iris = pd.read_csv(r"Iris.csv", names = columns)
print(iris)

le=LabelEncoder()
iris['code']=le.fit_transform(iris.Species)
print(iris)