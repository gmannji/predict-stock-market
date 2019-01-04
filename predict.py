import pandas as pd
from datetime import datetime

data = pd.read_csv('sphist.csv')
print(data.dtypes)
print(data.columns)
data['Date'] = pd.to_datetime(data['Date'])
print(data.dtypes)

print(data.head())
data.sort_values('Date',inplace=True,ascending=True)
print(data.head())