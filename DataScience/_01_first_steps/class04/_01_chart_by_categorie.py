import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
movies_csv_path = os.path.join(filedir, '..', 'datasets/tmdb-5000/tmdb_5000_movies.csv')

tmdb = pd.read_csv(movies_csv_path)

# That's a serie - It has an "index" and a "values" property
movies_by_language = tmdb.original_language.value_counts()
#print(movies_by_language)
movies_by_language_frame = movies_by_language.to_frame().reset_index()
movies_by_language_frame.columns = ['language', 'total']
print(movies_by_language_frame)

# Plot a bar chart specifying x/y dimensions
#sns.barplot(data = movies_by_language_frame, x='language', y='total')

# Auto-plot, based on inital dataframe, just specifying categorie
sns.catplot(x='original_language', data=tmdb, kind='count')
plt.show()