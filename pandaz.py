import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[value] = 0

for index, row in data.iterrows():
    value = row['whoAmI']
    data.at[index, value] = 1

data.head()