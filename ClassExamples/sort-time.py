# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:02:43 2021

@author: swamy

cpsc 242 homework 4
performance measurement
"""

import random  #use the random number library
import time  #use time library

#generate an arbitrary list of numbers
#sort the numbers, measure time

def genrand_sort(n):  # n - number of rand values

 rlist = []
 #gen. a list of rad nums between 1 and n
 for i in range(n):
    rlist.append(random.randint(1,n))

 #print(rlist)
 #get time before sorting
 init = time.time_ns()/1000000
 #sort list in place
 rlist.sort()
 #get time after sorting
 final = time.time_ns()/1000000

 print("n = ", n, "time (ms) : ", (final - init))

 #print(rlist)
 
##################################################
#call function with n = 130000
genrand_sort(45000)
   
