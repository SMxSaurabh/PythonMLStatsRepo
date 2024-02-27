# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:04:48 2023

@author: 91957
"""

import pandas as pd
import numpy as np
df=pd.read_csv("c:/2-dataset/loan.csv")

#Change all column to Same type
df = df.astype(str)
print(df.dtypes)

df.shape
#(39717, 111)
df.size
#4408587

df.describe()  
#[ 4 rows * 111 columns]

df.dtypes

#Covert all types to best possible type
df2=df.convert_dtypes()
print(df2.dtypes)
# o/p - All String

#Change all column to Same type
df = df.astype(int)
print(df.dtypes)

#Change type for one or multiple column
df = df.astype({"loan_amnt":int,"funded_amnt":float})
print(df.dtypes)

import pandas as pd
cols=['tax_liens','total_bal_ex_mort']
df[cols] = df[cols].astype('float')
df.dtypes

#Accesing one column
df['total_bc_limit']
##Accesing two column contents
df[['funded_amnt_inv','tot_hi_cred_lim']] 
#39717 rows * 2 column]
#Select certain rows and assign to another DataFrame
df2=df[4:]
df2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Drop column by index:
print(df.drop(df.columns[1],axis=1))



# using inplace=True
print(df.drop(df.columns[1],axis=1 ,inplace=True ))
print(df)

df2=df.iloc[2] #Select rows by index
df2
df2=df.iloc[[2,3,4]]  #Select rows by index list
df2
df2=df.iloc[1:5]     #Select rows by integer index range
df2
df2=df.iloc[:1]      #Select first row
df2
df2=df.iloc[:3]      #Select fist three rows
df2
df2=df.iloc[-1:]     #Select last row
df2
df2=df.iloc[-3:]     #Select last three rows
df2
df2=df.iloc[::2]     #Select alternate 2 rows


#Drop two or more column By index
df2=df.drop(df.columns[[0,1]], axis=1)
print(df2)



df1=df.drop(range(0,2))# It will delete 0 to 1
df1

#By using df[] notation
df2=df['term']
##Select multiple columns
df2=df.loc[['term','int_rate','installment']]

#Using loc[] to take column slices
#loc[] sytax too slice columns
#df.loc[:,start:stop:step]
#Select multiple columns
df2=df.loc[['term','int_rate','installment']]
#Select columns between two columns
df2= df.loc[:'term':'installment']
##Select column by range
df2=df.loc[:,'installment':]
#Select columns by range
#All the column up to Duration
df2=df.loc[:,:'installment']
df2





