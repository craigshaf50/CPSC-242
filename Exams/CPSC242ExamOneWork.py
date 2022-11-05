# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:09:55 2021

@author: craig
"""
'''i=0
sumNum=0
string='12efghc3'
strlist=list(string)
while i<len(strlist):
    n=strlist[i]
    if n=='0' or n=='1' or n=='2' or n=='3' or n=='4' or n=='5' or n=='6' or n=='7' or n=='8' or n=='9':
        convertlist=[0,1,2,3,4,5,6,7,8,9]
        n=convertlist[int(n)]
        sumNum=n+sumNum
        
    i=i+1
    print(sumNum)'''

str1='12ec3'
def add_char(sumNum,i):
    if i==-1:
        return sumNum
    n=str1[i]
    if n=='0' or n=='1' or n=='2' or n=='3' or n=='4' or n=='5' or n=='6' or n=='7' or n=='8' or n=='9':
        convertlist=[0,1,2,3,4,5,6,7,8,9]
        n=convertlist[int(n)]
        sumNum=n+sumNum
    else:
        sumNum=sumNum-2
    return add_char(sumNum,i-1)
    
print(add_char(0,4))

    
    