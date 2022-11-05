# -*- coding: utf-8 -*-
####################################################
# Homework 1 Problem D
# author: Craig Shaffer
# date revision: 1/12/21
# course: CPSC 242
#
# a function that takes 3 sets as parameters 
# and computes the intersection of the three sets
#
# input - three sets
# output - intersection of the three sets
#
####################################################

#three test sets
set_A={2,6,3,1,5,7}
set_B={1,3,8,7,9,5}
set_C={9,6,3,5,1,2}

#defines the intersection function with three parameters
def set_intersection(set1, set2, set3):
    #checks for intersection between first two sets
    tempSet=set1.intersection(set2)
    #checks for intersection between the third set and the temp set
    finIntersect=tempSet.intersection(set3)
    #returns the final intersection of the three sets
    return finIntersect
    
#calls the function and prints the result
print("The result of the intersection of the three sets is", set_intersection(set_A,set_B,set_C))
