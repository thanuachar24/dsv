import pandas as pd

# Read data from dataset
def getDataset(fname):
	df = pd.read_csv(fname)
	del df['Unnamed: 0']
	return df

# Q1 and Q3 Add columns for Average, Min and Max
def addColumns(df):
	df['Average'] = df.iloc[:,1:].mean(axis = 1)
	df['Min'] = df.iloc[:,1:-1].min(axis = 1)
	df['Max'] = df.iloc[:,1:-2].max(axis = 1)
	return df

# Q2 Add row which gives average monthly temperature
def addRow(df):
	df.loc['Average'] = df.iloc[:,1:-3].mean()
	return df

# Q4 Create dataframe called 'decade', storing 
#    average temperatures of each month in the respective decade.
def decadeDataframe(df):
	df = df.iloc[:-1,1:-3]

	data = []
	for i in range(0, 117, 10):
		if i != 110:
			data.append(list(df.iloc[i:i+10, :].mean().values))
		else:
			data.append(list(df.iloc[i:i+7, :].mean().values))
	decades = [i for i in range(1910, 2030, 10)]	
	months = list(df.columns)
	df_decade = pd.DataFrame(data, columns = months)
	df_decade['Decade'] = decades	

# Q5 Hottest year based on average temperature
def hottestYear(df):
	print (list(df[df['Average'] == df['Average'].max()].values)[0][0])

# Q6 Coldest year based on average temperature
def coldestYear(df):
	print (list(df[df['Average'] == df['Average'].min()].values)[0][0])

# Q7 Year recorded Min temperature
def yearMinTemperature(df):
	print (list(df[df['Min'] == df['Min'].min()].values)[0][0])	

# Q7 Year recorded Max temperature
def yearMaxTemperature(df):
	print (list(df[df['Max'] == df['Max'].max()].values)[0][0])	


def main():
	dset = getDataset('Weather Data in India from 1901 to 2017.csv')
	dset = addColumns(dset)
	dset = addRow(dset)
	decadeDataframe(dset)
	hottestYear(dset)
	coldestYear(dset)
	yearMinTemperature(dset)
	yearMaxTemperature(dset)

if __name__ == '__main__':
	main()