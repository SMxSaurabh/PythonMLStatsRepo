# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:43:31 2023

@author: 91957

"""
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
with open ('pi_digits.txt') as file_object:
    #The open function needs one argument : the name of
    #file you want to open 
    contents = file_object.read()
print(contents)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Observe the extra line at the end of output
#To avoid this rstrip method is used.
#rstrip method is used to remove, strps, any whitespace

with open ('pi_digits.txt') as file_object:
    #The open function needs one argument : the name of
    #file you want to open 
    contents = file_object.read()
print(contents.rstrip())
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Two types of path :
#   Relative path and absolute path
#In windows backward slash '\' and in linux OS front '/'.
#When you give relative path then need working directory

file_path='c:/1-python/pi_digits.txt'
with open(file_path) as file_object:
    contents= file_object.read()
print(contents.rstrip())
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
#Reading line by line
filename= 'pi_digits.txt' 
#we assign the name of the file we're reading from to the variable
with open(filename) as file_object:

#we again use with syntax to let python open and close 
#the file properly.
    for line in file_object:
        print(line)
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#
filename= 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#    
#Working with file contents.
filename= 'pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string +=line.strip()
        print(pi_string)
        print(len(pi_string))
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#writing to a file 
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊# 
#Writing multiiple lines
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new pages.")

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#  
#line appear on new line
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new pages.\n")

#📌~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~✏🖊#    
#Appending to a file
#Python does't erase the content of file.
filename='programming.txt'
with open(filename,'a') as file_object:
#WE use the 'a' argument to open the file for 
#appending rather than writting over existing file.
    file_object.write("I also love finding meaning in large dataset.\n")
    file_object.write("I love creating new apps that can run in browser.\n")
    
      
    
    
    
    
    
    
    
    
    

    
    
    













