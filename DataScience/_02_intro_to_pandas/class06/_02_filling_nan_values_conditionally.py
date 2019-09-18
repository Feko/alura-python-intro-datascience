import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/filtered.csv')

data = pd.read_csv(csv_path,sep=';')

properties_null_values = data[data['Valor'].isnull()]
data.dropna(subset = ['Valor'], inplace=True)

# Should remove entries with Condiminio NULL only if property type is 'Apartamento'
#print(data[data.Condominio.isnull()])
selection = (data['Tipo'] == 'Apartamento') & (data['Condominio'].isnull())
data = data[~selection]
data = data.fillna({'Condominio': 0, 'IPTU': 0})
print(data)

data.index = range(data.shape[0])

data.to_csv(os.path.join(filedir, '..', 'datasets/clean.csv'), sep=';', index=False)