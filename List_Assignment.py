# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:30:05 2023

@author: 91957
"""

#~~~~~~~~~~#
#Assignment#
#~~~~~~~~~~#
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
##[1]Take a 5 number in a list and find out minimum of
##list and maximum of list
def find_min_max(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num

numbers_list = [10, 5, 8, 3, 15]

min_number, max_number = find_min_max(numbers_list)
print("Minimum of the list:", min_number)
print("Maximum of the list:", max_number)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
##[2]Take 5 strings in list and make it reverse
def reverse_strings_in_list(strings_list):
    reversed_list = [string[::-1] for string in strings_list]
    return reversed_list
strings_list = ["hello", "world", "python", "programming", "example"]

reversed_strings = reverse_strings_in_list(strings_list)
print(reversed_strings)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
##[3]Take 10 numbers in a list .write script to search for
##a value
def search_value(numbers_list, value):
    if value in numbers_list:
        return f"Value {value} found in the list at index {numbers_list.index(value)}"
    else:
        return f"Value {value} not found in the list."


numbers_list = [23, 45, 12, 7, 89, 34, 67, 99, 15, 56]


search_value = int(input("Enter the search_value"))

result = search_value(numbers_list, search_value)
print(result)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
##[4] Take 10 numbers in the list insert some duplicates 
##Write script to find duplicates.
def find_duplicates(numbers_list):
    duplicates = []
    unique_numbers = set()
    
    for number in numbers_list:
        if number in unique_numbers:
            duplicates.append(number)
        else:
            unique_numbers.add(number)
    
    return duplicates


numbers_list = [23, 45, 12, 7, 89, 34, 7, 99, 15, 56]

duplicate_numbers = find_duplicates(numbers_list)
if duplicate_numbers:
    print("Duplicates found:", duplicate_numbers)
else:
    print("No duplicates found in the list.")
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
##[5] Take vowels in list and nonvowels in list .find 
##out total number of vowels in list.
def count_vowels(vowel_list):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    
    for char in vowel_list:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

mixed_list = ['a', 'b', 'e', 'f', 'i', 'k', 'o', 't', 'u']

total_vowels = count_vowels(mixed_list)
print("Total number of vowels in the list:", total_vowels)