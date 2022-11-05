# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:26:50 2021

@author: sponpandi
"""

def myproduct(a, b, c): #parameters of the functions
    
    d =  a * b * c
    
    return d

#main code
#arguments to the function call
prod = myproduct(2, 3, 4) # calling function myproduct 

print("product is ", prod)

x = 2
y = 3
z = 4

print("product is ", myproduct(x, y, z))
