import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/filtered.csv')

data = pd.read_csv(csv_path,sep=';')

# Properties of type 'Apartamento'
apartments = data[data.Tipo == 'Apartamento']

# Properties of type Casa
houses = data.query("Tipo in [ 'Casa', 'Casa de Condomínio', 'Casa de Vila']")

# Area between 60 and 100 m²
between_60_10 = data.query('Area >= 60 and Area <= 100')

# At least 4 bedrooms and rent < R$ 2000,00
four_bedrooms_cheap = data.query('Quartos >= 4 and Valor < 2000')
print(four_bedrooms_cheap)
print(four_bedrooms_cheap.shape[0])