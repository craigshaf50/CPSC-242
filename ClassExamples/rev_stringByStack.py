# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:16:56 2021

@author: swamy
reverses an input string using stack
"""

from stack import Stack

getstr = input("enter an input string to be reversed : ")

strstack = Stack()

i = 0

#push all chars from the string into stack
while(i < len(getstr)):
   strstack.push(getstr[i])
   i = i + 1

#print all chars from the stack by popping one at a time

while(not strstack.is_empty()):
   print(strstack.pop(),end='')

print('\n', end='')