# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:04:52 2023

@author: 91957
"""
#Series

import pandas as pd
songs2=pd.Series([145,142,38,13],name='count')
songs2.index
#It is easy to inspect the index of Series (or data)
#The index can be string as well
#in which case pandas indicates
#that the data types for the index is object(not string)

songs3= pd.Series([145,142,38,13],name='count',
                  index=['Paul','George','john','Ringo'])
songs3.index
songs3


#Numeric column will become NAN
import pandas as pd
f1=pd.read_csv('c:/1-python/age.csv')
f1

#If working directory is not selected then have to give absolute path
import pandas as pd
f1=pd.read_csv('age.csv')
f1

df=pd.read_excel('c:/1-python/Bahaman.xlsx')
df

# Numpy

import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
#142
numpy_ser[1]
#They both have method common
songs3.mean()
numpy_ser.mean()

#############################
#THE PANDA SERIES data structure provide
#support for the basic crud
#operations-create, read , update ,delete


#creation;
#Index should be unique

import panda as pd
george= pd.Series([10,7,8,1],
index=['1968','1969','1970','1971'],
name='George Songs')
george

#Reading 
#To read  or select data from a series
george['1968']

#We can iterate over data in a series
#as well , when iterating over a series

for item in george:
    print(item)

#Updating

george['1969']=68
george['1969']

#Deletion
s =pd.Series([2,3,4], index=[1,2,3])
del s[1]
s



#covert types
#string use.astypes(str)
#numeric use pd.to_numeric
#integer use .astype(int)
#Note that this will fall with NAN
#datetime use pd.to_datetime


import pandas as pd
songs_66=pd.Series([3,None,11,9],
index=['George','John','Paul','Ringo'],
name='count')
songs_66.dtypes
#dtypes('float')

pd.to_numeric(songs_66.apply(str))

#There will be error
pd.to_numeric(songs_66.astype(str), errors='coerce')
songs_66.dtypes
#Dealing with none
#The .fillna method replace them with a given value
songs_66.fillna(-1)
#NAN value can be drop using .dropna
songs_66.dropna()

#Append , combining and joining two series

songs_69=pd.Series([7,16,21,39],
index=['Ram','Sham','Ghansham','Krishna'],
name='Counts')
# TO concetenate two series together, 
#simply use the the .append()
songs=songs_66.append(songs_69)

#plotting two series

import matplotlib.pyplot as plt
#pylot is syb module and plt is alice name
fig = plt.figure()
songs_69.plot()
plt.legend()

#############
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()


#######################
import numpy as np
data= pd.Series(np.random.randn(500),name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
