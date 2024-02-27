# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:53:37 2023

@author: 91957
"""
#~~~~~~~~~~~~~~~~~~Tuple~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
tup1=(1,3,5,7)
#Accessing element of tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Tuples can hold differrent types 
tup2=(1,'john',True,-23.45)
print(tup2)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Iterating over tuples

tup3=('apple','orange','plum','mango')
for x in tup3:
    print(x)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Tuple related function
#You can count how many times a specified values
tup4=('apple','orange','plum','apple','mango')
#Tuple allow duplicates
tup4.count('apple')
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#find out index value of tuple
print(tup4.index('apple'))
print(tup4.index('orange'))
#check if element is exit 
if 'orange' in tup3:
    print('Orange is in the Tuple.')
#Nested Tuples
#Tuple can be nested within tuple
#Tuple can contain one of its element, another tuple.
tuple1=(1,3,5,7)
tuple2=('saurabh','sairaj','yash','sanchit')
tuple3=(42,tuple1,tuple2,23.5)
print(tuple3)
#It is not possible to add or remove element ,
#they are immutable