import pandas as pd
import os
import matplotlib.pyplot as plt
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/residential_rent.csv')

data = pd.read_csv(csv_path,sep=';')

group = data.groupby('Bairro')

print(group.describe().round(2))
# print(group['Valor'].aggregate(['min','max','sum']))

plt.rc('figure', figsize=(15,7))
# group['Valor'].std().plot.bar(color='blue')
fig = group['Valor'].mean().plot.bar(color='blue')
fig.set_ylabel('Rental Price')
fig.set_title('Mean Value', {'fontsize': 20})
plt.show()