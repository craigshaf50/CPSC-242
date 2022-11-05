# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:12:42 2021

@author: craig
"""

def is_palindrome(myString,begin_pos,end_pos):
    if begin_pos>=end_pos:
        return True
    return (myString[begin_pos]==myString[end_pos]) and is_palindrome(myString,begin_pos+1,end_pos-1)

string1='abcka'
print(is_palindrome(string1,0,len(string1)-1))