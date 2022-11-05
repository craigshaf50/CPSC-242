# -*- coding: utf-8 -*-
####################################################
# Homework 6 Problem 3
# author: Craig Shaffer
# date revision: 3/25/21
# course: CPSC 242
#
# A recursive binary search that passes the indices
# instead of slices of the array
#  
####################################################
Key = 9 
mlist1=[-23, -11, -7, -2, 1, 4, 5, 7, 12, 34, 56, 75]
mlist2 = [-23, -11, -7, -2, 1, 4, 5, 7, 8, 9, 12, 34]


def recBin_search(a_list,item,startIndex,endIndex):
    #if startIndex>endIndex then the item is not in the list
    if startIndex>endIndex:
        print('The Key does not exist in this list')
        return False
    midpoint=(startIndex + endIndex) // 2 #average of index
    #if a_list[midpoint] == item then the item is present in the list
    if a_list[midpoint] == item:
        print("index of Key = ", midpoint)
        return True 
    #if a_list[midpoint]<item then we only have to check numbers to the left of the midpoint
    elif item < a_list[midpoint]: 
        endIndex=midpoint-1
        return recBin_search(a_list, item, startIndex, endIndex)
    #if a_list[midpoint]>item then we only have to check numbers to the right of the midpoint
    else: 
        startIndex=midpoint+1
        return recBin_search(a_list, item, startIndex, endIndex)

#first list return false
print(recBin_search(mlist1,Key,0,len(mlist1)-1))

#secong list return true
print(recBin_search(mlist2,Key,0,len(mlist2)-1))