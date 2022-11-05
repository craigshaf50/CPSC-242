# -*- coding: utf-8 -*-
####################################################
# Homework 6 Problem 5
# author: Craig Shaffer
# date revision: 3/25/21
# course: CPSC 242
#
# Code to compute the ordinal value of words by
# adding the values of the characters. Then takes a
# mod value to determine the hash slot.
#  
####################################################

sumString=0 #initialize sum
string=input("enter string:") #gets input for word

#iterates through each character of the string and adds its value to the sum
for i in string:
    print(ord(i))
    sumString=sumString+ord(i)
    
#prints the sum of the ordinal value of the string
print("sum of",string,"is", sumString)

#number of hash slots
modVal=int(input("enter the mod for hashing:"))
#calculates where string belongs
hashSlot=sumString%modVal

#show math
print(sumString, "mod", modVal, "=", hashSlot) 
#tells which slot the string belongs in
print(string, "goes in slot ", hashSlot)