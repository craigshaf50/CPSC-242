# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:34:49 2021

@author: craig
"""

class complex_num:
    
    def __init__(self, real, imag=None):
        
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def get_sum(self, other):
        print("The sum is: ")
        return complex_num(self.real + other.real, self.imag + other.imag)
    
    def get_diff(self, other):
        print("The difference is: ")
        return complex_num(self.real - other.real, self.imag - other.imag)
    
    def get_prod(self, other):
        print("The product is: ")
        return complex_num((self.real * other.real) + (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))
    
    def get_quot(self, other):
        print("The quotient is: ")
        divisor = ((other.real)**2 + (other.imag/1j)**2)
        return complex_num(((self.real * other.real) -
        (self.imag * other.imag))/divisor,
        (((((self.imag)/1j) * other.real) - (self.real * (other.imag)/1j))*1j)/divisor)

    
c1 = complex_num(2,10j)
c2 = complex_num(3,5j)

c1.get_sum(c2)
c1.get_diff(c2)
c1.get_prod(c2)
c1.get_quot(c2)

