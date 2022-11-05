# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:18:20 2021

@author: swamy
fibonacci series using recursion
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2); n > 1

two versions
"""
#version 1
def fib(n):
   
    #return F(0)
    if(n < 1):
      return 0
    #return F(1)
    elif(n < 2):
      return 1
    #return F(n-2) + F(n-1)
    return fib(n - 2) + fib(n - 1)

print(fib(9))

#version 2
def fib1(n):
   
   #return F(1), F(0)
   if(n < 2):
      return [1,0]
  
   [x, y] = fib1(n - 1)
   
   return [x + y, x] 

print(fib1(14))

#what is the difference between version 1 and version 2? which one
#is better in terms of performance?
   