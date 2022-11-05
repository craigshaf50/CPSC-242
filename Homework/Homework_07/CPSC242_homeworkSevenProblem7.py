# -*- coding: utf-8 -*-
####################################################
# Homework 7 Problem 7
# author: Craig Shaffer
# date revision: 4/9/21
# course: CPSC 242
#
# Modify Instertion Sort to include Binary Search
# The binary search is implemented to find where 
# val should be placed in the sorted list
#  
####################################################

#binary search insertion sort
def bin_insertion_sort(a_list):
    for i in range(1, len(a_list)):
        val = a_list[i] #value to be placed
        pos = binary_search(a_list, val, 0, i-1) #place for value
        #recreates list after finding correct place for value
        #a_list=sorted smaller, value in correct place, sorted bigger, unsorted items
        a_list = a_list[:pos] + [val] + a_list[pos:i] + a_list[i+1:]
    return a_list #returns sorted list

#recursive binary search that passes first and last index
def binary_search(a_list, val, first, last):    
    #distinugish whether to insert before or after the left bound
    if first == last:
        if a_list[first] > val:
            return first
        else:
            return first+1
    if first > last:
        return first 
    midpoint = (first+last)//2 #find the midpoint
    #determine where val falls based on value of a_list[midpoint]
    #val is bigger than [midpoint], use right half of list and make another call
    if a_list[midpoint] < val: 
        return binary_search(a_list, val, midpoint+1, last)
    #val is smaller than [midpoint], use left half of list and make another call
    elif a_list[midpoint] > val:
        return binary_search(a_list, val, first, midpoint-1)
    else:
        return midpoint
    
    
MyList = [23, -12, -15, 10, 45, 3, 13, -19]
print(MyList)
print(bin_insertion_sort(MyList))