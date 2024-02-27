# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:18:04 2023

@author: Saurabh
"""

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#       
#Error and exception 
'''
#The error signifies the situation that mostly happen due 
to absence of system resources.

#Exceptions are handled with try-except block.
#Handling the ZeoDivisionError Exception.
'''
print(5/0)
#using try except block

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
# Using exception to prevent crashes.


#Handling the FileNotFoundError  Exception
filename= 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exit")
  
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 

#Json(Java sript object notation)

import json

numbers=[2,3,4,5,7,13]
filename='numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 

import json
username= input("What is your name? ")
filename ='username.json'
with open (filename,'w') as f:
    json.dump(username,f)
print(f"We'll remember you when you come back, {username}")

#########################################
#New program that greet's user whose name has already stored.
import json
filename ='username.json'
with open (filename) as f:
    username=json.load(f)
print(f"Welcome back, {username}!")

##########################################
#Load the user name ,if it has been stored previously
import json
filename='username.json'
try:
    with open (filename) as f:
        username=json.load(f)
        
except FileNotFoundError:
    username= input("What is your name? ")
    with open (filename,'w') as f:
        json.dump(username,f)
    print(f"We'll remember you when you come back, {username}")
    
else:
    print(f"Welcome back, {username}!")
    
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Write a python script to add a key to dictionary
#Sample Dictionary:{0:10,1:20}
#Expected result :{0:10,1:20,2:30}

d={0:10,1:20}
print(d)
d.update({2:30})
print(d)
###############
#Same code
d={0:10,1:20}
print(d)
d[2]=30
print(d)
##################################
'''
Write a python script to concatenate the following 
dictionary to create new one. 
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
Expected Result:{1:10,2;20,3:30,4:40,5:50,6:60}
'''

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):dic4.update(d)
print(dic4)
###################################
#Write python script to check whether a given key alredy
#exists in a dictionary.

def is_key_present(x):
    if x in d:
        print('Key is present in dictionary')
    else:
       print('Key is not present in dictionary') 
is_key_present(5)
is_key_present(8)
##################################

#Write a python progream to iterate over dictionary 
#using for loop
d={'x':10,'y':20,'z':30}
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)
    
#################################
















