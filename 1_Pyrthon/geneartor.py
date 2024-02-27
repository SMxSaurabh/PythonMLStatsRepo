# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:07:19 2023

@author: Saurabh
"""

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#  
####Generator####(Tuple)
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)#Show step by step output
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Function which return multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#now instead of using for loop we can
#write our own generator.
gen=range_even(6)
next(gen)
next(gen)
next(gen)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele *'*'
password=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(password)):
    print(password)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Enumerate

#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
##########################################
#same code can be implemented  using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate (lst,start=1):
    print(f"{index} {item}")
###########################################
def checkPassword(password):
    has_upper = False
    has_lower = False
    has_num = False

    # Check each character in the password and see which
    # requirement is met
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
        elif ch >= 'a' and ch <= 'z':
            has_lower = True
        elif ch >= '0' and ch <= '9':
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    else:
        return False

def hide_password(password):
    hidden_password = '*' * len(password)
    return hidden_password

p = input("Enter a password: ")
if checkPassword(p):
    print("Strong password")
else:
    print("Weak password")

hidden_p = hide_password(p)
print("Hidden password:", hidden_p)

#######################################################
#Examples:
#(1) Find all of the numbers from 1-1000 that
#are divisible by 7
div7=[n for n in range(1,1000) if n%7==0]
print(div7)
#######################################################
#(2) Find all of the numbers 1-1000 that have number
#3 in them
div3=[n for n in range(0,1000) if '3' in str(n)]
print(div3)
#######################################################
#(3) Count the number of spaces in string
some_string = 'The slow solid'
spaces =[s for s in some_string if s ==' ']
print(len(spaces))
######################################################
#(4) Create a list of all consonants in the string
sentence = '''Yellow Yaks like yelling and 
            yaming and yesterday they yodled while eating 
            yuks yams
           '''
result = [letter for letter in sentence if letter not in 'a,e,i,o,u," "' ]
print(result)
######################################################
#(5) Find the common number in two list(Without using 
#list or tuple)
list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[a for a in list_a if a in list_b]
print(common)
######################################################
'(Ready Reference)'
#(6) Get only the numbers in a sentence like 'In 1984
#there were 13 instance of a protest with over 1000
#people attending

sentence= ''' In 1984 there were 13 instance of a
 protest with over 1000 people attending
''' 
words= sentence.split()
result=[number for number in words if not number.isalpha()]
print(result)
################################################
##(Ready reference)

for n in range(20):
    if n%2 ==0:
        result.append('even')
    else:
        result.append('odd')
print(result)
 
##List comphrehension:
result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)
###################################################
"""
Produce a list of tuple
"""
list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a==b]
print(result)
###################################################
# H. W
def find_common_words(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    common_words = set(words1) & set(words2)
    return common_words

sentence1 = "The quick brown fox jumps over the lazy dog."
sentence2 = "A quick decision is better than a slow one."

common_words = find_common_words(sentence1, sentence2)
print("Common words:", common_words)

###################################################
'''
Find all the words in string that are less than 4 letters
'''
sentence='''On a summer day Ramnath sonar went
            swimming in the sun and his red skin stung
            '''
examine = sentence.split()
result=[word for word in examine if len(word) >=4]
print(result)

###############################################
#Write a python program to print a specified list
#After removing the 0th , 4th and 5th element
color=['Red','Green','White','Black','Pink','Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
#####################################################
#write a python program that creates a generator function
#that yields cubes of numbers from 1 to n.
#Accept n form user.
def cube_generator(n):
    for i in range(1,n+1):
        yield i ** 3 
#Accept th number from user
n=int(input("Input a number: "))
#Create the generator object

cubes=cube_generator(n)
#Iterate over the generator and print the cubes
print("cubes of numbers from 1 to",n)
for num in cubes:
    print(num)

######################################################
"""
Write a python program to implement a generator 
that generates random numbers within a given range
"""
import random
def random_number_generator(start, end):
    while True:
        yield random.randint(start, end)
#Accept input from user

start=int(input("Enter the start point: "))
end=int(input("Enter the end point: "))
random_numbers=random_number_generator(start,end)
print("Random numbers between",start,"and",end)
for _ in range(10):
    print(next(random_numbers))

#####################################################

#Write a python program to generate 3*4*6 
#3D array whose each element is *.
array=[[['*' for col in range(6)]for col in range(4)]for row in range(3)]
print(array)

####################################################
#write a python program to print the numbers of
# a specified list after removing even numbers from it.
num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)
####################################################
#~~~~~~~~~~~~Tuesday~~1_August_2023~~~~~~~~~~~~~~~~~~~~#
#Use of zip function
name=['dada','mama','kaka']
info=[9850,9579,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

###################################################
#Use of zip function with mis match list
name=['dada','mama','kaka','baba']
info=[9850,9579,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
#It will not display excess mismatch item in name
#i.e.baba

#################################################
#Zip_longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,9579,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
##################################################################
#use of fill value instead None
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,9579,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

#########################################################
#Use of all(), if all the values are true then 
#it will produce output
lst=[2,3,6,8,9]
if all(lst):
    print('all the values are true')
else:
    print('Useless')


#Value must be non zero,+ve,-ve

lst=[2,3,-6,8,9]
if all(lst):
    print('all the values are true')
else:
    print('Useless')

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
# all() method

lst=[2,3,-6,0,9]
if all(lst):
    print('all the values are true')
else:
    print('Useless')

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Use of any 'if any' one non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print('It has some value')
else:
    print("Useless")
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Use ' of any '
lst=[0,0,0,0,0]
if any(lst):
    print('It has some value')
else:
    print("Useless")

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Count

from itertools import count
counter = count()
print(next(counter))
print(next(counter))
print(next(counter)) 

#Now let us start from 1
from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Cycle()
# Suppose you have repeated tasks to be done, then you 
#can use this method

import itertools
instruction=("Eat","Code","Sleep")
for instruction in itertools.cycle(instruction):
    print(instruction)

#Repeat

from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Combination()

from itertools import combinations
players=['John','Jani','Janardhan']
for i in combinations(players,2):
    print(i)

#Permutations
from itertools import permutations
players=['John','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Product() 

from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['Virat','Manish','Shami']
for pair in product(team_a,team_b):
    print(pair)


#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Filter method

age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Shallow copy
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0] = -10
print(list_a)
print(list_b)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.copy(list_a)
# Affects the other!
list_a[0][0] = -10
print(list_a)
print(list_b)
#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[-10,2,3,4,5],[6,7,8,9,10]]

 
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Deep copy

list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.deepcopy(list_a)
# Affects the other!
list_a[0][0] = -10
print(list_a)
print(list_b)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
'''
Write a python program to create iterator
from several iterables in a sequence and display
the type and elements of the new iterator.

'''
from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)

#List
result = chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("Type of the new iterator: ")
print(type(result))
print("Elements of the new iterator: ")
for i in result:
    print(i)

#Tuple
result= chain_func((10,20,30,40),('A','B','C','D'),(40,50,60,70,80,90))
print("Type of the new iterator: ")
print(type(result))
print("Elements of the new iterator: ")
for i in result:
    print(i)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
'''
Write a python program that generates the running product 
of elements in an iterable.

'''
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)

#List
result= running_product([1,2,3,4,5,6,7])
print("Running product of list:")
for i in result:
    print(i)
    
#Tuple
result= running_product((1,2,3,4,5,6,7))
print("Running product of tuple:")
for i in result:
    print(i)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
'''
Write a Python program to contructs  an infinite iterator 
that returns evenly spaced values starting with a specified 
number and step.
'''
import itertools as it
start = 10
step= 1
print("The starting number is",start,"and step is",step)
my_counter=it.count(start,step)
#follow loop will run for ever.
#USE to generate similar kind of data.
print("The said function print never-ending items:")
for i in my_counter:
    print(i)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
'''
Write Python program to generate an infinite cycle
of elements from an iterable.
'''
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
#Following loop will run for ever
#List
result=cycle_data(['A','B','C','D'])
print("The said function print never-ending items: ")
for i in result:
    print(i)
#String
result=cycle_data('Python itertools')
print("The said function print never-ending items:")
for i in result:
    print(i)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#  
'''
Write a python program to make an iterator that drops
elements from the iterable as soon as an element is a 
positive number.
'''
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x : x<0,nums)
nums =[-1,-2,-3,4,-10,2,0,5,12]
print("Original list",nums)
result = drop_while(nums)
print("Drop elements from the iterable when a positive number arises \n",list(result))

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#  















