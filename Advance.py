# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:19:43 2023

@author: 91957
"""
##############################################
lst=[]
for num in range(0,20):
     lst.append(num)
     print(lst)
     
#We can write same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)
#################################################
#Capatalize Method make first letter capital
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)


###############################################
#List comprehension with if statment
def is_even(num):
    return num%2==0 
lst=[num for num in range(10) if is_even(num)]
print(lst)
#############################################
lst=[f"{x}{y}" for x in range(3)for y in range (3)]
#Execute first for loop the go to next for loop
print(lst)
#############################################








