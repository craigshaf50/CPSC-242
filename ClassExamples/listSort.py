# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:41:56 2021

@author: craig
"""

list1=[15,18,7,13]

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
            