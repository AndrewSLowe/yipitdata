import pandas as pd

file_name = r'/Users/andrewlowe/yipitdata/Q4_2013_Groupon_North_America_Data_XLSX.xlsx'
df = pd.read_excel(file_name)

# Q4_13_NA dataframe

Q4_13_NA = df

# (138534, 7) There are 138534 items in the dataframe. 

Q4_13_NA.shape

Q4_13_NA.describe()
Q4_13_NA.describe(exclude='number')
Q4_13_NA[]

segment_local = Q4_13_NA[(Q4_13_NA['Segment'] == 'Local')]
segment.shape

segment = Q4_13_NA[(Q4_13_NA['Segment'] == 'Local')]
