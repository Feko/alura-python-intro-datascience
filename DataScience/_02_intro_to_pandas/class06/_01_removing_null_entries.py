import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/filtered.csv')

data = pd.read_csv(csv_path,sep=';')

# 'Condominio' and 'IPTU' fields contains 'NaN'
#print(data.isnull())

properties_null_values = data[data['Valor'].isnull()]
data.dropna(subset = ['Valor'], inplace=True)