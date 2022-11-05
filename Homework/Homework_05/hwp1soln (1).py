# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:29:04 2021

@author: swamy

convert string to integer
example - '1234' (string) to 1234 (int)
"""

#use a dictionary to lookup the integer digit
#for a given character
#example, the digit correspinding to '0' is 
#obtained by str2int['0'] using the dictionary below
#
#start with the first character in the string and work our way 
#down to last. 
# '1234' -->  1 x 10^3 + 2 x 10^2 + 3 x 10^1 + 4
#       
#
def str2int1(mstr, pos):
   #dictionary
   str2int = {'0' : 0, '1':1, '2':2,
              '3':3, '4':4, '5':5,
              '6':6, '7':7, '8':8, '9':9}
   #recursion base case - no more string chars
   if(pos > len(mstr) - 1):
      return 0
   #multiply the digit by weight of the position (10^position_weight)
   return (str2int[mstr[pos]] * pow(10, len(mstr) - 1 - pos)) \
            + str2int1(mstr, (pos+1))

print('str2int1 --->', str2int1('2341', 0))

#start with the last character in the string and work our way
#to the first character
# '1234' = 4 x 10^0 + 3 x 10^1 + 2 x 10^2 + 1 x 10^3

def str2int2(mstr, pos):
    #dictionary
    str2int = {'0' : 0, '1':1, '2':2,
              '3':3, '4':4, '5':5,
              '6':6, '7':7, '8':8, '9':9}
   #recursion base case - no more string chars
    if(pos < 0):
      return 0
    #multiply the digit by weight of the position (10^position_weight)
    return str2int[mstr[pos]] * pow(10, len(mstr) - 1 - pos) \
      + str2int2(mstr, pos-1)

print('str2int2 --->', str2int2('1234', len('1234') - 1))
   
     