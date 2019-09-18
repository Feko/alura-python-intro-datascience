import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
ratings_csv_path = os.path.join(filedir, '..', 'datasets/ml-latest-small/ratings.csv')
movies_csv_path = os.path.join(filedir, '..', 'datasets/ml-latest-small/movies.csv')

ratings = pd.read_csv(ratings_csv_path)
movies = pd.read_csv(movies_csv_path)

print(movies.head())

# Query / Filtering the DataFrame
print(ratings.query('movieId==1').rating)
print(ratings.query('movieId==1').rating.mean())

# Grouping
mean_by_movie = ratings.groupby('movieId').mean()['rating']
print(mean_by_movie.describe())

#mean_by_movie.plot(kind='hist')
#sns.boxplot(mean_by_movie)
sns.distplot(mean_by_movie)
plt.show()