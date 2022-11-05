# -*- coding: utf-8 -*-
####################################################
# Homework 1 Problem E
# author: Craig Shaffer
# date revision: 1/13/21
# course: CPSC 242
#
# a phone book application using dictionary data
# type. The phone book stores the name and phone 
# number of individuals. The key for the phone book 
# is the person’s name and value is the person’s 
# phone number
#
####################################################

import sys

#initialize variables
option=0 
tempName=''

#Phonebook is dictionary type and starts out empty
#key is the name of person
#value is the phone number
phonebook = {}

#exit from the phone book
def exit_phone_book():
   print("Exiting the phone book...")
   print("---------------------------------------------------")
   sys.exit() #function call to quit the code and "close" the phone book
   
#delete an entry from the dictionary
def delete_entry(name):
   #check if name is in phone book using in operator
   if(name in phonebook):
       print("The entry ", name, " has been deleted")
       del phonebook[name]
   else:
       print("Error: ", name, "  does not exist in the phone book")   
   print("---------------------------------------------------")
   
#adds an entry to the dictionary  
def add_entry(name):
    #checks if name is not in the phone book
    if (name not in phonebook):
        #creates new entry in the dictionary
        phonebook[name]=input("Enter the new entry's number >> ")
        print("The entry ", name, " has been added")
    else:
        print("Error: ", name, " already exists in the phone book")
    print("---------------------------------------------------")

#displays the entries in the phone book
def display_phone_book():
    print(phonebook)
    print("---------------------------------------------------")


#infinite loop to display options for user
while(True):
   print("CPSC 242 Phone Book")
   print("Option 1 - display entries in the phone book")
   print("Option 2 - add an entry to the phone book")
   print("Option 3 - delete an entry from the phone book")
   print("Option 4 - exit the phone book")
   
   #gets the user input for choice of function
   option = int(input("enter your choice >> "))
   
   #uses user input gathered from option to call a function
   if(option == 4):
       exit_phone_book()
   elif(option == 3):
       tempName = input("Enter the name of the entry to delete >> ")
       delete_entry(tempName)
   elif(option==2):
       tempName = input("Enter the name of new entry >> ")
       add_entry(tempName)
   elif(option==1):
       display_phone_book()
