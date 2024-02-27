# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:06:34 2023

@author: 91957
"""

#Write a Numpy program to get the Numpy version abd show the Numpy
import numpy as np
print(np.__version__)

#-------------------------------------------------------#

#Write the Numpy program to test whether
#none of the elements of a given array are zero.
import numpy as np
x=np.array([1,2,3,4])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

x=np.array([0,1,2,3,])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write Numpy program Test if any of the 
#elements of the said array is non-zero
x=np.array([1,0,0,0])
print("Original array:")
print(x)
print("Test if any of the elements of the said array is non-zero:")
print(np.any(x))

x=np.array([0,0,0,0])
print("Original array:")
print(x)
print("Test if any of the elements of the said array is non-zero:")
print(np.any(x))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write Numpy program to test a given array element-wise
#for finiteness (not infinity or not a number)

import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original array:")
print(a)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write Numpy program to test element-wise for NAN of a given array.
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original array:")
print(a)
print("Test element wise for NAN:")
print(np.isnan(a))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
Write Numpy program to create an element wise comparison
(greater, greater_equal, less and less_equal) of two given 
arrays.
'''
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x,y))
print(np.greater_equal(x,y))
print("Comparison - less")
print(np.less(x,y))
print("Comparison - less_equal")
print(np.less_equal(x,y))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
Write Numpy program to create a 3X3 identity matrix.
'''
import numpy as np
array_2D=np.identity(3)
print('3x3 matrix:')
print(array_2D)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write Numpy program to generate a random number between
#0 and 1.
import numpy as np 
rand_num = np.random.normal(0,1,2)  
print("Random number between 0 and 1:")
print(rand_num)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#write a numpy program to create a 3X4 array and iterate 
#over it.
import numpy as np
a = np.arange(10,22).reshape((3,4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
    print(x,end=" ")
    print() 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write numpy program to create a vector of length 10 with 
#values evenly distributed between 5 and 50.

import numpy as np
v = np.linspace(10,49,5)
print("length 10 with alues evenly distributed between 5 and 50: ")
print(v)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Numpy program to create a 3x3 matrix with values
#ranging from 2 to 10.
import numpy as np
x = np.arange(2,11).reshape(3,3)
print(x)

#Error shows
import numpy as np
x = np.arange(2,10).reshape(3,3)
print(x)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write a numpy program to reverse an array 
#(The first element becomes the last.)
import numpy as np
x = np.arange(12,38)
print("Original array: ")
print(x)
print("Reverse array: ")
x = x[::-1]
print(x)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write the numpy program to compute the multiplication 
#of two given arrays.
import numpy as np
p=[[1,0],[0,1]] 
q=[[1,2],[3,4]]
print("Original matrix:")
print(p)
print(q)
result1 =np.dot(p,q)
print("Result of the said matrix multiplication:")
print(result1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write numpy program to compute the cross product of two given vectors.
import numpy as np
p=[[1,0],[0,1]] 
q=[[1,2],[3,4]]
print("Original matrix:")
print(p)
print(q)
result1 = np.cross(p,q)
result2 = np.cross(q,p)
print("Cross product of the said two vectors(p,q) :")
print(result1)
print("Cross product of the said two vectors(q,p) :")
print(result2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write a Numpy program to compute the
#determinentof a given sqaure array.

import numpy as np
from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write a numpy program to compute the eigenvalues and right 
#eigenvectors of a given square array.
import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix:")
print('a\n',m)
w,v=np.linalg.eig(m)
print("Eigenvalues of said matrix",w)
print("Eigenvalues of said matrix",v)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Write numpy program to compute the inverse of given matrix
import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result=np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



































