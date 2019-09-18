import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Feko -> Little hack to resolve CSV file path, independent of shell current dir
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/ml-latest-small/ratings.csv')

ratings = pd.read_csv(csv_path)

# Plot using pandas, which use matplotlib
# ratings.rating.plot(kind='hist')

# Plot using seaborn
sns.boxplot(ratings.rating)

plt.show()