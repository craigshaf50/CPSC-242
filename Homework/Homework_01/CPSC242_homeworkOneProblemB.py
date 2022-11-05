# -*- coding: utf-8 -*-
####################################################
# Homework 1 Problem B
# author: Craig Shaffer
# date revision: 1/12/21
# course: CPSC 242
#
# function to take a list of float numbers as a 
# parameter and calculate the average
#
# input - list of float numbers
# output - the average of the float numbers
#
####################################################

#list of float values for testing
floatList=[3.1, 2.0, 0.4, 1.7, 6.8, 1.2, 3.5, 2.3]

#defines the function for getting the average of the list in the parameter
def compute_average(fList):
    listSum=0 #initializes the variable to store the sum
    for i in fList:
        listSum=listSum+i #updates the sum
    average=listSum/len(fList) #calculates average (sum divided by length)
    
    return average #returns the value of the average to the function call
  
#calls the function      
print("The average of the list is ", compute_average(floatList))