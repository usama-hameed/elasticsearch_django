import pandas as pd

dataframe = pd.read_csv('wiki_movie_plots_deduped.csv')

data = dataframe.head(10)

print(data)