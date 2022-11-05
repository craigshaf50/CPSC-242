# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:01:08 2021

@author: swamy
demo of class type in python
"""

i = 0

1/2

#note the 'class' keyword 
class Fraction:
   
   #constructor function __init__
   #define the data in this class and default values
   def __init__(self, num, den):
      self.num = num
      self.den = den
      
   #print the data
   def print_Fraction(self):
      print(self.num,"/",self.den)
   
   #return numerator
   def get_num(self):
      return self.num

   #return denominator
   def get_den(self):
      return self.den

   def isequal(self, frac):
      if(self.num * frac.den == self.den * frac.num):
         print("Fractions are equal")
      else:
         print("Fractions are not equal")
   
   def sumfrac(self, frac):
      x = self.num * frac.den + self.den * frac.num
      y = self.den * frac.den
      
      return(x/y)
   
########main code
fraction1 = Fraction(3,5)

fraction1.print_Fraction()

print("numerator is : ", fraction1.get_num())

fraction2 = Fraction(6, 10)

fraction1.isequal(fraction2)

print("sum is : ", fraction1.sumfrac(Fraction(3,7)))