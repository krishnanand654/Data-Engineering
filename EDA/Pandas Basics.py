import pandas as pd
import numpy as np

first_series = pd.Series(list('abcdefg'))
print(first_series)

second_series = pd.Series(np.array(['A','B','C','D','E','F']))
print(second_series)

#By default index position will be auto incremented with start =0 and end= 8
#to change index position explictly (modified index)
second_series = pd.Series(np.array(['A','B','C','D','E','F']), index=['a','b','c','d','e','f'])
print(second_series)

#colletion of series
contry_per_capita = {'country':pd.Series(np.array(['A','B','C','D','E','F'])),
 'GDP per capita':pd.Series(np.array([167500,124200,39600,218316,474267,12552]))
 }

#creating dataframe using collection of series
GDP_DF = pd.DataFrame(contry_per_capita)

#Display first 5 rows
print(GDP_DF.head())



