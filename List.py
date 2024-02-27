# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:55:49 2023

@author: 91957
"""

#List

#List are mutable ordered containers of their objects.
#Creating List
list1=['apple','orange',31]
list2=[1,3,5,True]
root_list=['saurabh',list1,list2,'sanchit']
print(root_list)

#Accessing elements from list
list1=['saurabh','sairaj','yash','sanchit']
print('list1[1]:',list1[1])
print('list1[-1]:',list1[-1])
print('list1[1:3]:',list1[1:3])
print('list1[:3]:',list1[:3])
print('list1[1:]:',list1[1:])
#~~~~~~~# Append
list1.append('pete')
print(list1)
#~~~~~~# Extend
list1.extend(['albert','bob'])
print(list1)
#~~~~# Insert
#Insert into a list
a_list=['Adele','Madona','cher']
print(a_list)
a_list.insert(1,'paloma')
print(a_list)
#~~~~~~~~~~~~~# List concatenation

lst1=[3,2,1]
lst2=[6,5,4]
lst3=lst1+lst2
print(lst3)


#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#

#Removing from a list
another_lst=['Saurabh','Sairaj','Yash','Sanchit']
print(another_lst)
another_lst.remove('Sanchit')
print(another_lst)

#Pop method
#It takes an index which is the index of the item
#to remove from an item of list.
#It is different from remove.
another_lst=['Saurabh','Sairaj','Yash','Sanchit']
print(another_lst)
print(another_lst.pop(2))
print(another_lst)

#Insert
another_lst=['Saurabh','Sairaj','Yash','Sanchit']
print(another_lst)
another_lst.insert(1,'sidhant')
print(another_lst)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#













