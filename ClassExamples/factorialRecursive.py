# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:47:27 2021

@author: craig
"""


def factorial_N(n):
    if n<2:   #n is 1 or 0
        return 1
    return n*factorial_N(n-1)

print(factorial_N(5))


    