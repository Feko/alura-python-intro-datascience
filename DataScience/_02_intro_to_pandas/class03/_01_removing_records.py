import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/aluguel.csv')

data = pd.read_csv(csv_path,sep=';')

print(data['Tipo'].unique())
print(data.Tipo.drop_duplicates())