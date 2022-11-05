# -*- coding: utf-8 -*-
####################################################
# Homework 1 Problem A
# author: Craig Shaffer
# date revision: 1/12/21
# course: CPSC 242
#
# code to read 10 integers from the command prompt
# and compute the average of the 10 numbers
#
# input - 10 integers
# output - average of the integers
#
####################################################

#initialize variables
inputSum=0 #hold the sum of the user inputs
count=0 #counts number of inputs

#loop runs 10 times for 10 inputs
for i in range(10): 
    userInput=int(input("enter a number: ")) #accepts user input
    inputSum=inputSum+userInput #updates the sum with value of user input
    count=count+1 #updates count of iterations

#calculates and prints the average
print("The average of the user's inputs is >> ", inputSum/count)