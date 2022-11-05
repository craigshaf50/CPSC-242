# -*- coding: utf-8 -*-
####################################################
# Homework 4 Problem 2
# author: Craig Shaffer
# date revision: 2/12/21
# course: CPSC 242
#
# Using code from HW3 Q2, generate a arbitrary size 
# list between 1 and 25 using the random library. Then
# use the time library to measure the time taken by 
# your code.
#  
####################################################

import time #use the time library
import random #use the random library

#Homework 3 Question 2 Code
####################################################
#define function
def checkSum_for_25(numList):
    found=False #found is initialized to false
    for i in range(len(numList)):
        for j in range(len(numList)):      
            if numList[i]+numList[j]==25: #check if the values of i and j equal 25
                found=True #sets found to True if the values sum to 25
                print(numList[i], 'plus', numList[j], 'equals 25.')
    return found #if two numbers sum to 25, returns true
                 #if two numbers do not sum to 25, returns false
####################################################             
#new function to time the checkSum_for_25 function for n sized random list
def find_25time(n):
    ranList = [] #create empty list
    #generates a list of random nums between 1 and n
    for i in range(n):
        ranList.append(random.randint(1,25))
    #get time before looking for 25
    init = time.time_ns()/1000000
    checkSum_for_25(ranList)
    #get time after finding 25
    final = time.time_ns()/1000000
    print("n = ", n, "time (ms) : ", (final - init))
find_25time(100)

'''
#Updated Homework 3 Question 2 Code(Improved-faster time)
####################################################
#define function
def check_for_25(numList):
    found=False #found is initialized to false
    for i in range(len(numList)):
        for j in range(len(numList)):      
            if numList[i]+numList[j]==25: #check if the values of i and j equal 25
                print(numList[i], 'plus', numList[j], 'equals 25.')
                return True
    return found #if no values sum to 25 returns false

def find_new25time(n):
    ranList = [] 
    #generates a list of random nums between 1 and n
    for i in range(n):
        ranList.append(random.randint(1,25))
    #get time before looking for 25
    init = time.time_ns()/1000000
    check_for_25(ranList)
    #get time after finding 25
    final = time.time_ns()/1000000
    print("n = ", n, "time (ms) : ", (final - init))
find_new25time(100)
'''