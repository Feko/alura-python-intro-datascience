import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
movies_csv_path = os.path.join(filedir, '..', 'datasets/tmdb-5000/tmdb_5000_movies.csv')

tmdb = pd.read_csv(movies_csv_path)
print(tmdb.head())
print(tmdb.original_language.unique())
# tmdb.original_language => nominal categorical variable. 
# tmdb.budget => Quantitative variable
# tmdb.vote_cout => Quantitative variable
