# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:57:23 2023

@author: 91957
"""

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
################
##Creating Set##
################

##It won't allow duplicate element.apple print only once.
basket= {'apple','mango','apple','orange'}
print(basket)

#print every item of basket in new line
for item in basket:
    print(item)
    
#ADD #Alphabetically added
basket= {'apple','mango','orange'}
print(basket)
basket.add('banana')
print(basket)

#Update
#for adding more items then it passing through list 
basket= {'apple','mango','orange'}
basket.update(['banana','chikuu'])
print(basket)

#Obtaining the length of a set
basket={'apple', 'banana', 'mango', 'orange'}
print(len(basket))

#Find min and max
basket2={2,45,1,56,14}
print(min(basket2))
print(max(basket2))

#Removing an item
basket={'apple', 'banana', 'mango', 'orange'}
print(basket)
basket.remove('apple')
basket.discard('banana')
print(basket)

#Set operations
s1={'apple','mango','banana'}
s2={'orange','lime','banana'}
print('Union:', s1 | s2)
print('Intersection:',s1 & s2)
print('Difference:',s1 - s2)
