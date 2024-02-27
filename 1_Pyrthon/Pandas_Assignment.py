# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:15:21 2023

@author: 91957
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~#
#Assignment:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
1.Write a Pandas program to create a dataframe from a 
dictionary and display it
'''

import pandas as pd
d={'X':[75,56,67,78,90],'Y':[64,34,68,86,92],'Z':[78,32,61,84,96]}
df=pd.DataFrame(d);
print(df)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
2.Write a Pandas program to create and display a DataFrame
from a specified data
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'Attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data)
print(df)

df=pd.DataFrame(exam_data,index=labels)
print(df)


print(df.info)
df.describe()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
3.Write a Pandas program to get first 3 rows of DataFrame
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'Attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print(df)

print("First three rows of the dataframe:")
print(df.iloc[:3])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
4.Write a Pandas program to  select the 'name' and 'score'
column from DataFrame
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'Attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print(df)

print("Select the specific column:")
print(df[['name','score']])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
5.Write a Pandas program to select the specific column 
and rows from dataframe
Select specific rows and column:
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'Attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print(df)

print("Select the specific column:")
print(df[['score','Qualiphy']])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
6.Write Pandas program to select rows where the number
of attempts in the examination
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)

print("Number of attempts in the examination is greater than 2:")
print(df[df['attempts']>2])

#OR
df2=df.loc[df.attempts>2]
print(df2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
7.Write Pandas program to count the number of rows 
and columns of a DataFrame
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)

total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows:"+str(total_rows))
print("Number of Columns:"+str(total_cols))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
8.Write a Pandas program to select the rows where the 
score is missing.i.e NAN
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print(df[df['score'].isnull()])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
9.Write a search pandas program to select the  rows
the score is between 15 and 20 (inclusive).
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print("Rows where the score is between 15 and 20 (inclusive)")
df2=(df[df['score'].between(15,20)]) 
df2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
10.Write a search pandas program to select the rows 
where the number of attempts in the examination
is less than 2 and score greater than 15.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print('Write a search pandas program to select the rows where the number of attempts in the examinationis less than 2 and score greater than 15.')
print(df[(df['attempts']<2) & (df['score']>15)])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
11.Write a Pandas program to change the score 
in row 'd' to 11.5 .
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)

print("\n change the score in row 'd' to 11.5:")
df.loc['d','score']=11.5 #[row_name,column_name] 
print(df)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
12.Write a Pandas program to calculate the sum 
of the examination attempts by the student.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)

print("\n Sum of the examination attempts by the student: ")
print(df['attempts'].sum())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
13.Write a Pandas program to calculate the mean 
of all students scores.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)

print('\n Mean score of each different student in data frame: ')
print(df['score'].mean())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
14.Write a Pandas program to append a new row 'k'
to data fram with given values for each column.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[3,1,2,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)

print("Original rows:")
print(df)
print("\n Append new row:")
df.loc['k'] = ['Suresh','20.5','2','yes']
print("Print all records after insert a new records:")
print(df)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
15.Write a Pandas program to sort the DataFrame
first by 'name' in descending order,
then by 'score' in ascending order.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[19,7,16.5,np.nan,13,25,18,13.2],
    'attempts':[3,1,3,2,3,2,1,3],
    'Qualify':['no','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print("Original DataFrame")
print(df)
df = df.sort_values(by=['name'],ascending=[False])
print(df)
df = df.sort_values(by=['score'],ascending=[True])
print("Sort the data Frame first by descending order then by 'score' in ascending order.")
print(df)
#$$?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
16.Write Pandas program to replace the qualify column
conatins the values 'yes' and 'no' with True and False.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[2,1,3,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print("Original rows")
print(df)
print('Replace the qualify columnconatins the values yes and no with True and False: ')
df['Qualiphy'] = df['Qualiphy'].map({'yes': True,'no':False})
print(df)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
17.Write a Pandas program to change the name 
'Saurabh ' to viratin name column by DataFram. 
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[2,1,3,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print("Original rows")
print(df)
print("Change the name 'Saurabh' to 'Virat :")
df['name'] =df['name'].replace('Saurabh','Virat')
print(df)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
18.Write a Pandas program to insert 
a new column in existing DataFrame.
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[2,1,3,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
print("Original rows")
print(df)
color=['Red','Blue','Orange','Green','Pink','White','Black','Grey']
df['color']=color
print("New DataFrame after inserting the 'color' column ")

print(df)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
Write a Pandas program to iterate over rows in a DataFrame
'''
import pandas as pd
import numpy as np
exam_data={
    'name':["Saurabh","Ravi","Sanchit","Pratik","Sidhant","Sairaj","Prashant","Kunal"],
    'score':[13,7,16.5,np.nan,25,19,18,13.2],
    'attempts':[2,1,3,2,3,2,1,3],
    'Qualiphy':['yes','no','yes','yes','no','yes','yes','no'],    
}
labels=['a','b','c','d','e','f','g','h']
df=pd.DataFrame(exam_data,index=labels)
df
for index,row in df.iterrows():
    print(row['name'],row['score'])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
















