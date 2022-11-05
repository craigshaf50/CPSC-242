# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 08:41:10 2021

@author: sponpandi

recursive code for reversing a string
4 different versions

The first two versions use explicit index to partition
the string by removing one character at a time

The last two versions use Python slices which implicitly
pass the index to the recursive function

"""

def revstring1(mstr, i):

   if(i < 1):
      return mstr[0]

   return mstr[i] + revstring1(mstr, i - 1)

print('revstring1 -->', revstring1('home', len('home')-1))

def revstring2(mstr, i):

   if(i > len(mstr) - 2):
      return mstr[len(mstr)-1]

   return revstring2(mstr, i + 1) + mstr[i]

print('revstring2 -->', revstring2('home', 0))

def revstring3(mstr):

   if(len(mstr) < 2):
      return mstr

   return mstr[len(mstr)-1] + revstring3(mstr[0:len(mstr)-1]) 

def revstring4(mstr):

   if(len(mstr) < 2):
      return mstr

   return revstring4(mstr[1:]) + mstr[0] 



