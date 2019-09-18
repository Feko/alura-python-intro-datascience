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

ratings_movie_1 = ratings.query('movieId==1')
ratings_movie_2 = ratings.query('movieId==2')

print('Average rating of Movie #1 - %.2f, with a deviation of %.3f' % (ratings_movie_1.rating.mean(), ratings_movie_1.rating.std()))
print('Average rating of Movie #2 - %.2f, with a deviation of %.3f' % (ratings_movie_2.rating.mean(), ratings_movie_2.rating.std()))

