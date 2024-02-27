# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:16:46 2023

@author: 91957
"""

#~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~#
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "The number is not prime"
            break
    return "The number is prime"
print(prime_num(12))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Functions without argument
def greet_user():
        print("Hello!")#Display simple Greeting
greet_user()
#~~~~~~~~~~~~~~~Passing information to function~~~~~~~~~~~~~~~~~~~~~~~~#
def greet_user(username):
    print(f"Hello,{username}!")
greet_user('Sanjivani AI')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Positional Argument animal_type and pet_name
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('Dog','Moti')
#Order matter in positional argument
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Returning Dictionary Arguments
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('ram','sarkar')
print(musician)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#passing list
def greet(names):
    for name in names:
        msg=f"hello , {name.title()}!"
        print(msg)
username=['ram','sham']
greet(username)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#passing arbitary number of arguments
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#now we can replace the print() with loop that runs 
#through the list of toppings nd describe the pizza being ordered:
    
def make_pizza(*toppings):
#Summarize the pizza we are about to make."""
    print("\n Making pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Mixing positional and arbitary arguments
##################~~~~~~~~~~~~~~~####################~~~!!!!!
def make_pizza(size,*toppings):
#Summarize the pizza we are about to make."""
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')  
######~~~~~~~~~~##########~~~~~~~~~~~~~~~###########~!!!!!!!!!
#crearte a pizza file and access that file


import pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#importing specific functions
from pizza import make_pizza 
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')  


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#using as to give a functions an Alias
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#using as to give a Module an Alias
import pizza as p 
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Importing all functions in a module
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Scope of variable
x=6
x=x+1
print(x)
#~~~~~~~~~~~~~~~##########~~~~~~~~~~~~~~~~~###############
#lambda function
#name of function = lambada then argument passing (i.e-> a,b,c) : buisness logic(a+b+c)
#add=lambda a,b,c:a+b+c
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def mul(a,b,c):
    mul=a*b*c
    return mul
print(mul(4,5,6))
mul=lambda a,b,c:a*b*c
mul(4,5,6)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
val=lambda *args:sum(args)
val(1,2,3,4,5,6)
val(1,2,3,4,5,6,7,8,9)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#

# Two types of argument : keyword arguments and 
#non keyword argument can be pass in python function
#There are special symbole assigned to represent keyword 
#argument and non keword argument
# *args (Non keyword argument)
# **kwargs(Keyword argument)

#*args in function defination in python is used to pass 
# a variable number of argument to afunction .It is 
#used to pass non-keyword,variable-length argument list.
#Dictionary contain {key: value}
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#data is in the form of dictionary
def person(name,**data):
    print(name)
    print(data)
person(name='Navin',age=28,place='Mumbai',mob_no=998867)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Name and every data on new line 
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='Navin',age=28,place='Mumbai',mob_no=998867)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
max=lambda a,b:x if(a>b)
print(max(1,2))
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
max=lambda a,b:x if(a>b) else b
print(max(1,2))
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
max=lambda a,b:x if(a>b) else b
print(max(8,10))
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Python collection types
#Tuple
#list
#Dict
#set
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#














