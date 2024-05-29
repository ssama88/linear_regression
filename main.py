import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split as split
# from sklearn.linear_model import LinearRegression

data = pd.read_csv('adult.csv')

print(data.head(5))
# print(data.info())
# print(data.columns)

# x = data[['age', 'education', 'occupation', 'relationship']]

# y = data['fnlwgt']

# one, two, three, four = split(x,y,test_size=0.35)
