# -*- coding: utf-8 -*-
####################################################
# Homework 1 Problem C
# author: Craig Shaffer
# date revision: 1/12/21
# course: CPSC 242
#
# function named that takes two arbitrary list of strings
# as parameters, and merges the two lists into a larger 
# list by alternating the items from each list
#
# input - two lists of strings
# output - the merged string
#
####################################################

#test lists of strings
stringListOne=['Craig', 'a', 'of', 'Denver']
stringListTwo=['is', 'fan', 'the', 'Broncos']

#defines the function with parameters of two lists
def merge_list(list1, list2):
    
    mergedList=[] #initializes the merged list
    i=0 #loop/index counter
    
    #infinite loop to run through as many items that are in the lists
    while True:
        #if the list has a value for that index it will be added to the list
        if i<len(list1):
            mergedList.append(list1[i])
        #if the list has a value for that index it will be added to the list
        if i<len(list2):
            mergedList.append(list2[i])
        i=i+1 #updates loop/index counter
        #if there are no more values to be added from either list, stops infinite loop
        if i>=len(list1) and i>=len(list2):
            break
    return mergedList #returns the merged list

#function call and prints the result
print("The merged list is ", merge_list(stringListOne, stringListTwo))

