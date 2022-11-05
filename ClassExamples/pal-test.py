# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:10:28 2021

@author: swamy
"""

from mydeque import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
