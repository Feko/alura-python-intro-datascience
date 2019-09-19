import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/clean.csv')

data = pd.read_csv(csv_path,sep=';')

# Creating a brand-new column
data['Total Value'] = data['Valor'] + data['Condominio'] + data['IPTU']

# A couple more
data['Value Per m2'] = (data['Valor'] / data['Area']).round(2)
data['Gross value Per m2'] = (data['Total Value'] / data['Area']).round(2)

# One using lambda
data['Aggregate Type'] = data['Tipo'].apply(lambda x: 'House' if 'Casa' in x else 'Apartment')


print(data.head(100))