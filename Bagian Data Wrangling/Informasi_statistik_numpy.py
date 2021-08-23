# Menampilkan informasi statistik dengan Numpy

import pandas as pd 

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print(csv_data.describe(include='all'))

# Filter Numerical karena ada Nan

import pandas as pd 

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print(csv_data.describe(exclude=['O']))
