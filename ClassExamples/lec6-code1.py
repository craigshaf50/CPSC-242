# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:05:23 2021

@author: swamy
"""

mlist = [1, 3, 5, 7, 9]

def add(partial_sum, i):
   
   if(i == -1):
      return partial_sum
   
   next_item = mlist[i];
   
   partial_sum = next_item + partial_sum
   print(partial_sum, i)
   return add(partial_sum, i-1)


print(add(0,len(mlist)-1))