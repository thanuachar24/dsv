import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('match.csv')
country = list(df['Country'].unique())
colors = ['blue', 'yellow', 'green', 'red', 'orange']

colour = {}
for i in range(len(country)):
	colour[country[i]] = colors[i]

fig, ax = plt.subplots()
grouped = df.groupby('Country')

for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Matches', y='Avg',  label=key, color=colour[key])    

for i in range(6):
	plt.text(df.iloc[i,3], df.iloc[i,4], df.iloc[i, 0])
plt.show()