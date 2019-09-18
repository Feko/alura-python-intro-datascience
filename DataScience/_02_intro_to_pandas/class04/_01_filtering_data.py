import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/aluguel.csv')

data = pd.read_csv(csv_path,sep=';')

property_type = data['Tipo'].drop_duplicates()
#print(list(property_type))
housing_types = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
filtered_dataset = data[data['Tipo'].isin(housing_types)]
filtered_dataset.index = range(filtered_dataset.shape[0])
print(filtered_dataset)