# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:58:12 2023

@author: 91957
"""

##############
##Dictionary##
##############

capitals={
'Maharashtra':'Mumbai',
'gujrat':'Amahadabad',
'UP':'Lukhnow',
'Karnataka':'Banglore',
'Andhrapradesh':'Hydrabad'    
}
print(capitals)

#Accessing items using keys
print('capitals[Maharashtra]:',capitals['Maharashtra'])

#Adding new entry
capitals['West_Bengal']='Kolkatta'  
capitals
#Changing key value
capitals['Gujrat']='Gandhinagar'
print(capitals)     

#Removing entry
capitals.pop('Karnataka')
print(capitals)  

#also
del capitals['UP']                                                                                                           
print(capitals)

#Iterating 
capitals={
'Maharashtra':'Mumbai',
'gujrat':'Amahadabad',
'UP':'Lukhnow',
'Karnataka':'Banglore',
'Andhrapradesh':'Hydrabad'    
}

#keys
for states in capitals:
    print(states, end=',')
#Keys value    
for states in capitals:
    print(states, end=':')
    print(capitals[states])
#Value, keys and items
print(capitals.values())  
print(capitals.keys()) 
print(capitals.items()) 


#Checking key Membership
print('Karnataka' in capitals)
print('Bihar' not in capitals)

#Obtaining the length of dictionary
print(len(capitals))

####
#Dictionary can have values in tuple
seasons ={'Summer':('Feb','Mar','Apr','May'),
'Rainy':('June','July','August','Sept'),
'Winter':('Oct','Nov','December','January')
}
print(seasons['Rainy'])
print(seasons['Rainy'][0])



#Dictionary methods
#get method is useful method to access the 
print(capitals.get('UP'))
#values of a key in a dictionary
#Duplicates are not allow in dictionary and set.
#Dictionary can't have same items with same key.
#Take only once.
dict2={"brand":"maruti",
       "model":"breeza",
       "year":2021,
       "year":2020
       
       }
print(dict2)

#Loop through dictionary, it will show only keys
for x in dict2:
    print("key: ",x)
#print all values in the dictionary, one by one:
for x in dict2:
    print("Values: ",dict2[x])   
    
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Wrte python program to add all items in the list

def sum_list(items):
   sum=0 
   for x in items:
       sum=sum+x
      
   return sum
print(sum_list([5,6-8]))
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
