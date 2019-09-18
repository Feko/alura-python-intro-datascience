import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
movies_csv_path = os.path.join(filedir, '..', 'datasets/tmdb-5000/tmdb_5000_movies.csv')

tmdb = pd.read_csv(movies_csv_path)

total_by_language = tmdb.original_language.value_counts().to_frame().reset_index()
total_by_language.columns = ['language', 'total']
print(total_by_language)

# Pie chart
# plt.pie(total_by_language['total'], labels=total_by_language['language'])


total_by_language = tmdb.original_language.value_counts()
total = total_by_language.sum()
total_en = total_by_language['en'].sum()
total_remaining = total - total_en
data = {
    'language' : ['English', 'Other'],
    'total' : [total_en, total_remaining]
}
data = pd.DataFrame(data)
sns.barplot(data=data, x='language', y='total')
plt.show()