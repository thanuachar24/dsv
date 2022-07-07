import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('test.csv')

plt.scatter(df['Balls'], df['Runs'], s=df['Wickets'])
plt.xlabel('Balls')
plt.ylabel('Runs')
plt.title('Bowling Analysis')

plt.show()
