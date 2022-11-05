# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:03:36 2021

@author: swamy ponpandi
phone book application using dictionary
homework 1, Part E, cpsc 242A/B

"""

import sys

#phonebook dictionary data type
#key = name
#value = phone numbers
#both data are strings
phonebook = {'tom':'456-451-6785', 
             'susan':'123-671-8903'}

choice = 0;
delname = ''

#quit from program
def exit_phone_book():
   sys.exit() #function call to quit python code

#delete entry from dictionary
def delete_entry(name):
   #check if name is in phone book using in operator
   if(name in phonebook):
      del phonebook[name]
   else:
      print("error : ", name, "  does not exist")
   
   print("------------------------------")

############################################################
######Your functions for add_entry, display_phone_book below





#############################################################


#main part of code
# a infinite while loop displays choices to the user

print("Phone book - CPSC 242")

while(True):
   
   print("Choice 1 - display phone book")
   print("Choice 2 - add entry")
   print("Choice 3 - delete entry")
   print("Choice 4 - exit")
   
   choice = int(input("enter your choice - "))
   
   if(choice == 4):
      exit_phone_book()
   elif(choice == 3):
      delname = input("enter the name to delete : ")
      delete_entry(delname)
      