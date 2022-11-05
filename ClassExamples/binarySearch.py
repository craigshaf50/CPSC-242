# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:02:57 2021

@author: craig
"""


Key = 9 
mlist1=[-23, -11, -7, -2, 1, 4, 5, 7, 12, 34, 56, 75]
mlist2 = [-23, -11, -7, -2, 1, 4, 5, 7, 8, 9, 12, 34]
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        print('first', first, 'last', last)
        midpoint = (first + last) // 2
        print("mid", midpoint)
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

#print(binary_search(mlist,Key))

def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        print('midpoint',midpoint)
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            print(a_list[:midpoint])
            return binary_search_rec(a_list[:midpoint], item)
        else:
            print(a_list[midpoint + 1 :])
            return binary_search_rec(a_list[midpoint + 1 :], item)
        
print(binary_search_rec(mlist2, Key))        







