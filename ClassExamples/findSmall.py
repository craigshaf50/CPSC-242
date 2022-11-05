# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:41:56 2021

@author: craig
"""
# O(n^2) parabolic growth - T(n) ~= 2n^2 + 5n + 1

list1=[15,18,7,13]
'''
def find_smallest(mylist):
    i=0
    while i<len(mylist):
        temp_small=mylist[i]
        j=0
        small_check=True
        while j<len(mylist): #goes through list of items
            if temp_small>mylist[j]:
                small_check=False
            j=j+1
        if small_check:        
            smallest=temp_small
            print("current statement is smallest")
        i=i+1
    return smallest

print(find_smallest(list1))
'''


#O(n) linear growth - T(n) ~= 2n + 2

def get_smallest(mylist):
    i=0
    tempSmall=mylist[0]
    while(i<len(mylist)):
        if tempSmall>mylist[i]:
            tempSmall=mylist[i]
        i=i+1
    return tempSmall
print(get_smallest(list1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    