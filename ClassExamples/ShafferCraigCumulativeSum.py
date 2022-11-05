# -*- coding: utf-8 -*-
####################################################
# Class Activity
# author: Craig Shaffer
# date revision: 1/12/21
# course: CPSC 242
#
# code to compute cumulative sum of integers
#
# input - integers
# output - the sum of these integers
#
####################################################

#initial value of the sum
sum=0

#infinite loop to continue to accept user input
while(True):
    numVal = input("enter an integer or 'done' >> ")
    if(numVal == "done"): #checks if user input "done"
        print("sum is: ", sum)
        break #ends infinite loop
    sum = sum + int(numVal) #adds integer to cumulative sum