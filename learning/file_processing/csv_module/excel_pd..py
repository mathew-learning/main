import pandas as pd

data = pd.read_excel('sample.xlsx')
# print(type(data))
print(data[0])
print(data.head())
print(data.tail())