# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:04:18 2021

@author: craig
"""

from stack import Stack

list1=[33,45,23,4,7]
list2=['+','-','*','+']

#create two empty stacks
stack1=Stack()
stack2=Stack()

#populate stack1
while (len(list1)>0):
    item1=list1.pop()
    stack1.push(item1)
    stack1.print_stack()
stack1.print_stack()

#populate stack2
while (len(list2)>0):
    item2=list2.pop()
    stack2.push(item2)
    stack2.print_stack()
stack2.print_stack()

#pop 2 items off top 1, 1 off 2
totItems=0
while stack1.size()>1 and stack2.size()>0:
    firstItem=stack1.pop()
    secondItem=stack1.pop()
    operand=stack2.pop()
    if (operand=='+'):
        totItems=firstItem+secondItem
        stack1.push(totItems)
    elif (operand=='-'):
        totItems=firstItem-secondItem
        stack1.push(totItems)
    elif (operand=='*'):
        totItems=firstItem*secondItem
        stack1.push(totItems)
    print(totItems)
print(totItems)
        

