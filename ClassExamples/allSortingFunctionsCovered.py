# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:07:37 2021

@author: craig
"""

def bubble_sort(a_list):
    for i in range(len(a_list) - 1):
        for j in range(len(a_list) - 1 - i):
            if (a_list[j] > a_list[j + 1]):
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
    return a_list

def bubble_sort_opt(a_list):
    for i in range(len(a_list) - 1):
        exchange = False
        for j in range(len(a_list) - 1 - i):
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
                exchange = True
        if(exchange == False):
            break
    print('num. iterations = ', i)
    return a_list

def selection_sort(a_list):
    for i in range(len(a_list)-1):
        max_idx = 0
        for j in range(len(a_list) - i):
            if a_list[j] > a_list[max_idx]:
                max_idx = j
        a_list[max_idx], a_list[len(a_list) - 1 - i] = \
            a_list[len(a_list) - 1 - i], a_list[max_idx]

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val

def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        #Merge
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)
def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
            a_list[right_mark],
            a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    return right_mark