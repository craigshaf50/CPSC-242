# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:20:07 2021

@author: craig
"""

def sequential_search(a_list, item):
    pos = 0
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            pos = pos + 1
    return False

def ordered_sequential_search(a_list, item):
    pos = 0
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            if a_list[pos] > item:
                return False
            else:
                pos = pos + 1
    return False

def binary_search(a_list, item): 
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)


