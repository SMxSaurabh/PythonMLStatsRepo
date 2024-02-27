# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:25:23 2023

@author: 91957
"""

#Assignment#
import datetime

def remaining_time_until_80(birth_date):
    today = datetime.date.today()
    age_at_80 = birth_date.year + 80 - 1  
    target_date = datetime.date(age_at_80, birth_date.month, birth_date.day)
    remaining_days = (target_date - today).days

    remaining_months = remaining_days // 30
    remaining_weeks = remaining_days // 7

    return remaining_days, remaining_weeks, remaining_months

def main():
    try:
        birth_year = int(input("Enter your birth year (YYYY): "))
        birth_month = int(input("Enter your birth month (MM): "))
        birth_day = int(input("Enter your birth day (DD): "))

        birth_date = datetime.date(birth_year, birth_month, birth_day)
        remaining_days, remaining_weeks, remaining_months = remaining_time_until_80(birth_date)

        print(f"Until you turn 80 years old:")
        print(f"Days left: {remaining_days}")
        print(f"Weeks left: {remaining_weeks}")
        print(f"Months left: {remaining_months}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for year, month, and day.")

if __name__ == "__main__":
    main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def roller_coaster_ticket_price(age, height):
    if height >= 120:
        if age < 12 or age < 15:
            return 15
        elif age >= 18 and height > 120:
            return 50
        else:
            return 20
    else:
        return None

def main():
    try:
        age = int(input("Enter your age: "))
        height = int(input("Enter your height in cm: "))

        ticket_price = roller_coaster_ticket_price(age, height)

        if ticket_price is not None:
            print(f"Your ticket price for the roller coaster is Rs. {ticket_price}.")
        else:
            print("Sorry, you are not eligible to play on the roller coaster.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for age and height.")

if __name__ == "__main__":
    main()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##########################################################
print("Welcome to the roller coaster")
height=int(input("Please enter your height in cm: "))
bill=0 
if height>=120:
    print("Your eligible for roller coaster")
    age=int(input("Please enter your age:"))
    if age<12:
        print("Child tickets are $5")
        bill=5
    elif age<=18:
        print("Youth ticket are $7")
        bill=7
    else:
        print("Adult ticket are $12")
        bill=12
    want_photo=input("Do you want Y or N: ")
    if want_photo=='Y':
        bill+=3
        print(f"Your total bill will be {bill} ")
    else:
        print(f"you total bill {bill}")
else:
    print("Sorry next time !")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
users=["admin","employee","manager","worker","staff"]

for user in users:
    if user=="admin":
        print("Hello admin, would you like to see a report status?")
    elif user=="employee":
        print("Hello employee")
    elif user=="manager":
        print("Hello manager")
    elif user=="worker":
        print("Hello worker")
    else:
        print("Hello")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import string
#pick the adjective
adjectives=['sleepy','slow','smelly',
            'wet','fat','red','orange',
            'yellow','green','blue','purple',
            'fluffy','white','proud','brave']
#pick the nouns
nouns=['apple','dianasour','ball','toaster',
       'goat','dragon','hammer','duck','panda']

import random
adjective = random.choice(adjectives)
noun=random.choice(nouns)
number=random.randrange(0,100)
special_char=random.choice(string.punctuation)
password = adjective + noun +str(number)
print("Your new password is: %s"% password)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("Welcome to password picker!")
while True:
    adjectives = random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password = adjective + noun +str(number)
    print("Your new password is: %s"% password)
    response= input("would you generate another password y or n:")
    if response =='n':
        break
    else:
        print("Your new password is: %s"% password)   
        
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
#Check each character in th password and see which
#requirement meet
    for ch in password:
        if ch>='A' and ch<='Z':
            has_upper=True
        elif ch>='a' and ch<="z":
            has_lower=True
        elif ch>='0' and ch<='9':
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
p=input("Enter a password: ")
if checkPassword(p):
    print("Strong password")
else:
    print("Weak password")
        
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print("What is ypur today's age")
years_today=input("years :")
months_today=input(" months :")
days_today=input(" days :")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"your total age today in days {total_days_today}")
print("Let us assume you are expected to live 90 years")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"Your remaining life in days {remaining_days_to_live}")

###########################################
#Assignments/:
print("Welcome to the pizza hut ")
size_pizza=input("Please enter the size of pizza,S,M,L: ")
add_pepp=input("Do you want to add pepp enter y :  ")
extra_cheese=input("Do you want to add extra cheese then enter y: ")
bill=0
if size_pizza=='S':
    print("You choose $3 small pizza!")
    bill=3
    print(f"Your bill is {bill}.")
elif size_pizza=='M':
    print("You choose $7 medium pizza!")
    bill=5
    print(f"Your bill is {bill}.")
elif size_pizza=='L':
    print("You choose $10 medium pizza!")
    bill=10
    print(f"Your bill is {bill}.")    
if add_pepp=='y':
    print("You have add the pepp")
    bill+=3
if extra_cheese=='y':
    print("You have add the pepp")
    bill+=3
    print(f"According to the your order your bill is {bill}") 
else:
    print(f"According to the your order your bill is {bill}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#