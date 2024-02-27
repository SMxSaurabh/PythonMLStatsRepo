# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:09:46 2023

@author: 91957
"""

#Prime Number
user_input = input("Enter a number: ")

number = int(user_input)
if number <= 1:
    print(number, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


##########################################
#Leap Year
year_input = input("Enter a year: ")

if year_input.isdigit():
    year = int(year_input)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print("Invalid input. Please enter a valid year as an integer.")
################################################
#String is palindrom or not
user_input = input("Enter a string: ")


cleaned_string = ''.join(char.lower() for char in user_input if char.isalnum())


if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#####################################################
#Mario pyramid - Dowmward
def print_mario_pyramid_downward(height):
    for i in range(height, 0, -1):
        blocks = "#" * i
        print(blocks)

height_input = int(input("Enter the height of the downward Mario Pyramid: "))
print_mario_pyramid_downward(height_input)

#Mario Pyramid - Left Side
def print_mario_pyramid_left_side(height):
    for i in range(1, height + 1):
        blocks = "#" * i
        print(blocks)

height_input = int(input("Enter the height of the left side Mario Pyramid: "))
print_mario_pyramid_left_side(height_input)

#Mario Pyramid- Right Side
def print_mario_pyramid_right_side(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        blocks = "#" * i
        print(spaces + blocks)

height_input = int(input("Enter the height of the right side Mario Pyramid: "))
print_mario_pyramid_right_side(height_input)

#Mario Pyramid - Upward
def print_mario_pyramid_upward(height):
    for i in range(height, 0, -1):
        spaces = " " * (height - i)
        blocks = "#" * (2 * i - 1)
        print(spaces + blocks)

height_input = int(input("Enter the height of the upward Mario Pyramid: "))
print_mario_pyramid_upward(height_input)

#Mario Pyramid - Complete Upward
def print_mario_pyramid_complete_upward(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        blocks = "#" * (2 * i - 1)
        print(spaces + blocks)

    for i in range(height - 1, 0, -1):
        spaces = " " * (height - i)
        blocks = "#" * (2 * i - 1)
        print(spaces + blocks)

height_input = int(input("Enter the height of the complete upward Mario Pyramid: "))
print_mario_pyramid_complete_upward(height_input)


#Mario Pyramid - Complete Downward
def print_mario_pyramid_complete_downward(height):
    for i in range(height, 0, -1):
        spaces = " " * (height - i)
        blocks = "#" * (2 * i - 1)
        print(spaces + blocks)

    for i in range(2, height + 1):
        spaces = " " * (height - i)
        blocks = "#" * (2 * i - 1)
        print(spaces + blocks)

height_input = int(input("Enter the height of the complete downward Mario Pyramid: "))
print_mario_pyramid_complete_downward(height_input)

########################################################

for i in range(4):
    for j  in range(4):
        print("#",end=' ')
    print()
################################   
    for i in range(4):
        for j in range (i+1):
            print("#",end=" ")
#################################  
n=int(input("Enter the number:"))    
for i in range(n):
    for j in range(n-i):
        print("#",end=' ')
    print()
#################################