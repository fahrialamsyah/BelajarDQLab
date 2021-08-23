#Akses range pada suatu kolom dan baris tertentu
import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print("Menampilkan data ke 5 sampai kurang dari 10 :")

print(csv_data['Age'].iloc[5:10])

#Menampilkan suatu range data tertentu pada suatu baris saja

import pandas as pd 

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print("Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris:")

print(csv_data.iloc[5:10])
