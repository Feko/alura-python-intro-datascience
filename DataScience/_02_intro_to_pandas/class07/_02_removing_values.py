import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/clean.csv')

data = pd.read_csv(csv_path,sep=';')

data['Total Value'] = data['Valor'] + data['Condominio'] + data['IPTU']
data['Value Per m2'] = (data['Valor'] / data['Area']).round(2)
data['Gross value Per m2'] = (data['Total Value'] / data['Area']).round(2)
data['Aggregate Type'] = data['Tipo'].apply(lambda x: 'House' if 'Casa' in x else 'Apartment')

df = pd.DataFrame(data[['Total Value', 'Value Per m2', 'Gross value Per m2', 'Aggregate Type']])

# Removing a column using del
del df['Total Value']

# Removing using pop
df.pop('Gross value Per m2')

# Removing using drop
df.drop(['Aggregate Type'], axis=1, inplace=True)

print(df.head(100))

# Export to use in next lessons
data.drop(['Total Value', 'Gross value Per m2'], axis=1, inplace=True)
data.to_csv(os.path.join(filedir, '..', 'datasets/residential_rent.csv'), sep=';', index=False)