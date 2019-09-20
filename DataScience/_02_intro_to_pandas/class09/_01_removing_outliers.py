import pandas as pd
import os
import matplotlib.pyplot as plt
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/residential_rent.csv')

data = pd.read_csv(csv_path,sep=';')

plt.rc('figure', figsize=(15,7))
#data.boxplot(['Valor'])
#print(data[data['Valor'] > 500000])
values = data['Valor']

Q1 = values.quantile(.25)
Q3 = values.quantile(.75)
IIQ = Q3 - Q1
lower_bound = Q1 - 1.5 * IIQ
upper_bound = Q3 + 1.5 * IIQ

selection = (values >= lower_bound) & (values <= upper_bound)
new_data = data[selection]

#new_data.boxplot(['Valor'])
new_data.hist(['Valor'])
plt.show()