## Data lengkap maka outputnya false
import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print(csv_data.isnull().values.any())

## Data tidak lengkap maka outputnya true
import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")

print(csv_data.isnull().values.any())
