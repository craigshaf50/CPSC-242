# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:34:27 2021

@author: swamy

while loop demo
"""

# basic while loop construct
# count = 5
# i = 0

# while (i < count):
#     print(i)
#     i = i + 1

# compound while condition
# count = 5
# i = 0
# done = ''

# while( i < count and done != 'quit'):
#     print(i)
#     done = input("give me an input : ")
#     i = i + 1

#nested while loops
count1 = 3
count2 = 5
i = 0
j = 0

while(i < count1):
    print("i = ", i, " j  = ", end='')
   
    j = 0
    while(j < count2):
      print(j, end='')
      j = j + 1
      
    i = i + 1
   
    print("\n", end='')
    
# print("hello", end='')
# print("cpsc 242")    