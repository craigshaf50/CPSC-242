# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:08:07 2021

@author: craig
"""

def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]
print(rreverse("good day"))