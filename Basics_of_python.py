# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:21:56 2023

@author: 91957
"""
##################################
x=1
print(x)
print(type(x))
x=1000000001
print(x)
print(type(x))
##################################
age=input('Plaese enter your age:')
print(type(age))
print(age)
##################################
age1=input('Please enter your age:')
print(type(age1))
print(age1)
age2=input('Please enter your age:')
print(type(age2))
print(age2)
age=age1+age2
print(age)
##################################

age1=int(input('Please enter your age:'))
print(type(age1))
print(age1)
age2=int(input('Please enter your age:'))
print(type(age2))
print(age2)
age=age1+age2
print(age)

###################################
#floating point numbers

exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))

##################################
#Type casting

int_value=100
string_value='1.5'
float_value=float(int_value)

print('int value as a float:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))

###################################
#Complex Numbers

c1=1
c2=2j
print('c1:',c1 ,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
print(c1+c2)
#####################################

#Boolean Values

all_ok=True
print(all_ok)
all_ok= False
print(all_ok)
print(type(all_ok))

##########################################

#String into Boolean
status = bool(input('Ok it is confirmed?: '))
print(status)
print(type(status))

##########################################
#Arithmatic opearators

home=10
away=15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
###########
goals_for=10
goals_against=7
print(goals_for-goals_against)
print(type(goals_for-goals_against))
##########

print(100/20)
print(type(100/20))
###########

print(100//20)
print(type(100//20))

#But if we find remainder theb need modulus operator
print('Modulus division 100%13:',100%13)
print('Modulus division 3%2:',3%2)

#Power Operator is'**'
a=5
b=3
print(a**b)

#Assignment Operator
x = 0
x += 1 #has the same behaviour as x=x+1 also known as compound operator

#None value

winner = None
print(winner is None)
#Alternatively
print(winner is not None) 

#which will print out only if the

winner=None
print('winner:',winner)
print('winner is None:',winner is None)
print('winner is not None:',winner is not None)
print(type(winner))
print('Set winner to True')
winner = True
print(winner)
##############################################
#Flow of Control

num=int(input('Enter a number: '))
if num >0:
    print(num)
#############

if num<0:
    print("Its negative")
else :
    print("its positive")
#######################
#USE of elif
saving = float(input("Enter how much you have in saving?: "))
if saving == 0:
    print("Sorry no saving")
elif saving < 500:
    print("Well done")
elif saving < 1000:
    print("That's a tidy sum:")
elif saving < 10000:
    print("Welcome sir:")
else:
    print("Thank You!")
##########################
#While loop
count = 1
print('Starting ')
while count <=10:
    print(count)
    count+=1
#############################
#For loop
print('Print out the value in the range')
for i in range(2,10):
    print(i)
    print('Done')
########################
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0,16):
    if i==num:
        break
    print(i)
print('Done')
########################
#Use of an 'anonymous' variable
for _ in range(0,10):
    print('.',end='')
    print()
    
#######################

for _ in range(0,10):
    print('.',end='')
########################################
#Location of print is changed
for i in range (0,6):
    if i==num:
        break
    print(i,' ',end='')
    print('Done')
#######################################
#Python program to print odd number in given range
start,end=4,19

#iterating each number in list
for num in range(start,end+1):
    #check condition
    if num % 2!=0:
        print(num, end=" ")


#######################################
#print even numbers
start=int(input("Enter the one numberr:"))
end=int(input("Enter the second numberr:"))
for num in range(start,end+1):
    #check condition
    if num % 2==0:
        print(num, end=" ")
#############################################
for even_numbers in range(4,15,2):
    #here inside range function first no denotes starting,
    #second denotes end
    #third denotes the interval
    print(even_numbers,end=' ')
##############################################
for odd_numbers in range(4,15,2):
    #here inside range function first no denotes starting,
    #second denotes end
    #third denotes the interval
    print(odd_numbers+1,end=' ')
####################################
#Global Variable 
x='Awesome'
def my_function():
    print("python is:"+x)
my_function()

#################################
#Local and Global Variable
x='Awesome'
def my_function():
    x='Fantastic'
    print("python is " +x)
my_function()
print("python is "+x)
###################################
#Dictionary

x={"name":"ram","age":34}
print(type(x))
####################################

str1='Hello'
str2=2
str3=str1+str2

#TypeError: can only concatenate str (not "int") to str

##########################################
#If you want multiple line
x="""This is Python.
It is very powerful"""
print(x)

#-----------------------------------------------#
#String Slicing
x="""This is Python.
It is very powerful"""

print(x[2:7])
#-------------------------------------------------#
#-----------------slice from the start------------#
x="""This is Python.
It is very powerful"""
print(x[:7])
#------------------Slice to the end-------------#
x="""This is Python.
It is very powerful"""
print(x[4:])
#--------------------negative indexing----------#
x="""This is Python.
It is very powerful"""
print(x[-5:-2])
#negative indexing start from 'end to start'.Like -1,-2,-3......

#modify string
x="""This is Python.
It is very powerful"""
print(x.upper())
#______________________#
x="""This is Python.
It is very powerful"""
print(x.lower())

#__________-Remove White Space-___________#
x="""    This is Python.
It is very powerful  """
print(x.strip())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
x="Hello World"
print(x.replace("Hello","Gello"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Use of split that replace the white space/or ,
x="Hello,world"
print(x.split(","))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
x="Hello world"
print(x.split(" "))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
x="Hello world"
string1=x[::-1]
print(string1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#find method,Searches the string for a specified value and returns the position
 
x="This is Python and It is very powerful"
print(x.find("and"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#String concateness with space
x="hello"
y="world"
print(x+" "+y)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#f operator
x=36
y="My name is anthony"
print(x+y)#It will give error

print(f"My name is anthony and my age is {x}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number {item_no},its price is {price}")

#~~~~#
quantity=3
item_no=54
price=67
my_order="I want {} pieces and item number {},its price is {}"
print(my_order.format(quantity,item_no,price))
#~~~~~~~~#
#The escape character allows you to use double quotes when you normally would
text="This is fun fair and it has got big \"round rigo\""
#text=This is fun fair and it has got big "round rigo"
print(text)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#operator procedure
print(3*3+3/3-3)
#~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~#

#Rule for mathematical operations
#PEMDAS
#P-parenthesis
#E-Exponetial
#M-Multiplication
#D-Division
#A-Addition
#S-Substraction

#~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~#