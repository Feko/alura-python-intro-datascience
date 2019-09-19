import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/residential_rent.csv')

data = pd.read_csv(csv_path,sep=';')

neighborhoods = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selection = data.Bairro.isin(neighborhoods)
data = data[selection].drop_duplicates()

group = data.groupby('Bairro')
for bairro, dados in group:
    print('{} -> {}'.format(bairro, dados['Valor'].mean().round(2)))

print(group['Valor'].mean().round(2))