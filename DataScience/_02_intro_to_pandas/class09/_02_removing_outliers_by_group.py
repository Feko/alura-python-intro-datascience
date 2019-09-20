import pandas as pd
import os
import matplotlib.pyplot as plt
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/residential_rent.csv')

data = pd.read_csv(csv_path,sep=';')
plt.rc('figure', figsize=(15,7))

group = data.groupby('Tipo')['Valor']

Q1 = group.quantile(.25)
Q3 = group.quantile(.75)
IIQ = Q3 - Q1
lower_bound = Q1 - 1.5 * IIQ
upper_bound = Q3 + 1.5 * IIQ

# print(Q1)
# print(Q3)
# print(lower_bound)
# print(upper_bound)

df = pd.DataFrame()
for t in group.groups.keys():
    selection = (data['Valor'] >= lower_bound[t]) & (data['Valor'] <= upper_bound[t]) & (data['Tipo'] == t)
    df = pd.concat([df,data[selection]])

df.boxplot(['Valor'], by=['Tipo'])

plt.show()