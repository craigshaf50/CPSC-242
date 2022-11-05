# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:32:28 2021

@author: swamy
cpsc 242 spring 2021
example modified from textbook
"""
#convert an integer to string data type
def to_str(n):
   convert_string = "0123456789"
   if n < 10:
      return convert_string[n]
   else:
      return to_str(n // 10) + convert_string[n % 10]

#main code
x = 1453
print(type(x), x)
x = to_str(1453)
print(type(x), x)