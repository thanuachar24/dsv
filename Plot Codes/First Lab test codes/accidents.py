import pandas as pd

df = pd.read_csv('./road accidents/Road_accidents.csv')
df_time = pd.read_csv('./road accidents/Road_accidents_time.csv')
#print (df)

# 2.	Which state has highest number of accidents in year 2013?
df['Total'] = df.iloc[:,2:].sum(axis = 1)
df2013 = df[df['YEAR'] == 2013]
print(df2013[df2013['Total'] == df2013['Total'].max()]['STATE/UT'])

# 3.	Find the average monthly accidents for each state.
#monthly_accidents = df.groupby(['STATE/UT'])['JANUARY','FEBRUARY','MARCH','APRIL', 'MAY']

#4.	Which month has highest accidents?
print (df.iloc[:,2:-1].sum().idxmax())

# 5.	Which time slot (like 0-3, 3-6 etc) has more accidents?
print (df_time.iloc[:,2:].sum().idxmax())

#5a. Time slots with more accidents in state 'Karnataka'
print (df_time[df_time['STATE/UT'] == 'Karnataka'].iloc[:,2:].sum().idxmax())

# 6.	Which state has more accidents from year 2001 to 2014?
print (df[df['YEAR'] <= 2014].groupby(['STATE/UT'])['Total'].sum().idxmax())

# 7.  List states whose accidents number in year 2014 is less than 
#     state average from 2001 to 2014.
state_avg = df.groupby(['STATE/UT'])['Total'].mean()
df_2014 = df[df['YEAR'] == 2014][['STATE/UT','Total']]
df_2014.index = df_2014['STATE/UT']
del df_2014['STATE/UT']
df_2014 = df_2014.squeeze()
state_avg.drop(['D & N Haveli','Delhi (Ut)'], inplace=True)

print (df_2014[state_avg > df_2014].index)

# 8.	Which month has more accidents over the year?
print (df.iloc[:,2:-1].mean().idxmax())





