# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:33:15 2021

@author: swamy
"""

from stack import Stack

code = input("enter a line of code for syntax checking : ")

syntax_stack = Stack()

i = 0

while(i < len(code)):
   
   if(code[i] == '('):
      syntax_stack.push(code[i])
   elif(code[i] == ')'):
      if(syntax_stack.size() <= 0):
       print("error 1 - syntax error mismatched paranthesis")
       break
      
      syntax_stack.pop()
      
   i = i + 1
      
if(syntax_stack.size()):
   print("error 2 - syntax error mismatched paranthesis")