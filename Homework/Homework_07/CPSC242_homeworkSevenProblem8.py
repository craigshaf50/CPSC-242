# -*- coding: utf-8 -*-
#############################################################
# Homework 7 Problem 8
# author: Craig Shaffer
# date revision: 4/9/21
# course: CPSC 242
#
# Descending Order Selection Sort:
# Modify the selection sort code to get descending order.
# This can be done by flipping the greater than sign (>) to
# a less than sign (<).
#  
#############################################################

#Descending Selection Sort
def dec_selection_sort(a_list):
    for i in range(len(a_list)-1):
        max_idx = 0
        for j in range(len(a_list) - i):
            if a_list[j] < a_list[max_idx]: #Change > to < in order to get descending order
                max_idx = j
        a_list[max_idx], a_list[len(a_list) - 1 - i] = \
            a_list[len(a_list) - 1 - i], a_list[max_idx]
    return a_list


#Original Selection Sort Code from Slides (Ascending)
def selection_sort(a_list):
    for i in range(len(a_list)-1):
        max_idx = 0
        for j in range(len(a_list) - i):
            if a_list[j] > a_list[max_idx]:
                max_idx = j
        a_list[max_idx], a_list[len(a_list) - 1 - i] = \
            a_list[len(a_list) - 1 - i], a_list[max_idx]
    return a_list

MyList = [23, -12, -15, 10, 45, 3, 13, -19]
print(MyList)
#print(selection_sort(MyList))
print(dec_selection_sort(MyList))
