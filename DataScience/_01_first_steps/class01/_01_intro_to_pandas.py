import pandas as pd
import os
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/ml-latest-small/ratings.csv')

# This create a Pandas DataFrame
ratings = pd.read_csv(csv_path)

# Feko -> It's possible to override columns names
# ratings.columns = ['usuarioId', 'filmeId', 'nota', 'timestamp']

print(ratings.head())
print(ratings.shape)

# That's no longer a DataFrame, but a serie
series = ratings['rating']

print(series)
print(series.unique())
print(series.value_counts())
print(series.mean())
print(series.median())
print(series.describe())