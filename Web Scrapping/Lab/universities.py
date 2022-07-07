import pandas as pd
import matplotlib.pyplot as plt

# Get Table data to dataframe
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_universities_in_India')

# To CSV
df[0].to_csv('universities.csv', index=False, header = True)



df_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_institutions_of_higher_education_in_Karnataka#Universities')

df_tables[0].to_csv('Institutes of National Importance.csv', index=False, header = True)
df_tables[1].to_csv('Institutes of Eminence.csv', index=False, header = True)
df_tables[2].to_csv('Central.csv', index=False, header = 5)
df_tables[3].to_csv('Deemed to be University.csv', index=False, header = True)
df_tables[4].to_csv('State.csv', index=False, header = True)
df_tables[5].to_csv('Private.csv', index=False, header = True)

d1 = df_tables[3].groupby('Location').count()
places = list(d1.index)
loc_count = list(d1.University)

fig1, ax1 = plt.subplots()
ax1.pie(loc_count, labels = places)
plt.show()


df1 = df[0].sort_values(by='Total', ascending=False)
df2 = df1.head(6).iloc[1:,:]
df2.plot.bar(x ='State', y = 'Total')
plt.show()