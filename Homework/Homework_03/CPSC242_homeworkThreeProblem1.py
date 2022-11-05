# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem 1
# author: Craig Shaffer
# date revision: 2/4/21
# course: CPSC 242
#
# A function to determine the kth smallest integer 
# in a list that is given in increasing order
#  
####################################################

#defines the function taking a list and k value as parameters
def find_kth_smallest(numList, k):
    if k>0 and k<=len(numList): #checks if the k value works with the length of the given list
        return numList[k-1] #returns the number in the list that is the kth smallest
    else:
        return print("The kth smallest integer doesn not exist. Please enter a valid number for k.")

#testing 
testList=[1,3,4,5,7,9,12,18,23,30,34,45,56,93,109]
print('The kth smallest integer in the list is', find_kth_smallest(testList, 2))