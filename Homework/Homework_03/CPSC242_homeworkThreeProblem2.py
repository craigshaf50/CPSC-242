# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem 2
# author: Craig Shaffer
# date revision: 2/4/21
# course: CPSC 242
#
# A function to find two values in a list that sum
# to 25. The upper bound of this function must be
# O(n^2).
#  
####################################################

#define function
def checkSum_for_25(numList):
    found=False #found is initialized to false
    for i in range(len(numList)):
        for j in range(len(numList)):      
            if numList[i]+numList[j]==25: #check if the values of i and j equal 25
                found=True #sets found to True if the values sum to 25
                print(numList[i], 'plus', numList[j], 'equals 25.')
    return found #if two numbers sum to 25, returns true
                 #if two numbers do not sum to 25, returns false


#tests for certain outputs
#testing: returns true
randomList=[1,2,4,13,10,14,20,12,5]
print("Are there two numbers that exist in the list that sum to 25?", checkSum_for_25(randomList))

#testing: returns false
failureList=[1,2,3,4,12,16,17,11,20]
print("Are there two numbers that exist in the list that sum to 25?", checkSum_for_25(failureList))