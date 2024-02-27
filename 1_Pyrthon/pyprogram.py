# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:34:50 2023

@author: 91957
"""
#📌~~~Thursday~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Write python program to multiply all the items in the list
def list_mul(items):
    mul=1
    for x in items:
        mul=mul*x
        
    return mul
print(list_mul([1,5,-8]))
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
'''
Q.Write a python program to get the largest number
from a list.'''
def find_min_max(numbers):
    
    max_num = max(numbers)
    return  max_num

numbers_list = [10, 5, 8, 3, 15]

max_number = find_min_max(numbers_list)

print("Maximum of the list:", max_number)
'''Q.Write a python program to count the number of strings
which satisfies the condition that the string length 
is 2 or more and the first and last character from a
 given list of string.'''
def match_words(words):
    ctr=0
    for word in words:
        if len(word) > 2 and word[0] ==word[-1]:
            ctr +=1
    return ctr
print(match_words(['abc','xyz','aba','1221']))

'''
Q. Write a python program to get a list,sorted in 
increasing order by the last element in each tuple from given list
of non-empty tuples.
sample list=:[(2,5),(1,2),(4,4),(2,3),(2,1)]
Expected result:[(2,1),(1,2),(2,3),(4,4),(2,5)]
'''
def last(n):
    return n[-1]
def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))
'''
Q.Write a program to remove duplicate from the list.
'''
lst1=[10,20,30,20,10,50,60,40,80,50,40]
st1=set(lst1)
#Since set removes duplicates items,hence list is
#converted to set
print(st1)
lst2=list(st1)
print(lst2)

'''
Write a python program to clone or copy a list

'''
original_list=[10,27,44,23,4]
new_list=list(original_list)
print(original_list)
print(new_list)

'''
Write a python program to find the list of words that are 
longer than n form a given list of words.
'''
def long_words(n,str):
    word_len=[]
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jump over the lazzy dog"))


'''
Write a python function that takes two list and returns
True if they have  at least  one comman member.
 
'''
def common_data(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x ==y:
                result = True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))            
print(common_data([1,2,3,4,5],[6,7,8,9]))  

'''
Write python program to calculate difference betwwen two 
lists.
'''
list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
total_diff=diff1+diff2
print(total_diff)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
###########
'''
Write python program to convert a list of characters 
into a string
'''    
###########
s=['a', 'b', 'c', 'd']
str1=''.join(s)
print(str1)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
'''
Write a python program to find the index of an item
in a specified list.
'''

num=[10,30,4,-6]
print(num.index(30))
#Used in recommdation engine.
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
'''
Write a python program to append a list to the 
second list
'''

list1=[1,2,3,0]
list2=['Red','Green','Black']
final_list = list1 + list2
print(final_list)

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#