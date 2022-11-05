# -*- coding: utf-8 -*-
####################################################
# Class Activity
# author: Craig Shaffer
# date revision: 1/12/21
# course: CPSC 242
#
# determine if stringTwo is a substring of stringOne
#
# input - two strings
# output - true or false depending on if stringTwo is
#          a substring of stringOne or not
#
####################################################

#strings for testing
stringOne= 'denverbroncos'
stringTwo='verbronc'

def checkSubString(string1,string2):
    list1=list(string1)
    list2=list(string2)
    listfound=[] #stores found characters of stringTwo within stringOne
    i=0 #loop counter
    found=0 #counts the number of found characters
    while(i<len(list1)): #while loop to find characters
        if(list1[i]==list2[found]):
            print(list2[found]) #prints the found characters
            listfound.append(list2[found])
            found=found+1 #updates characters found
            if(found==len(list2) and listfound == list2):
                return True
        else:
            found=0 #resets the found counter
            print("the character is not part of the substring")
            listfound=[] #resets the list of found characters    
        i=i+1 #updates the loop counter
    if found==0 and i==len(list1):
        return False

#function call
print("Is the stringTwo a substring of stringOne?", checkSubString(stringOne,stringTwo))
    