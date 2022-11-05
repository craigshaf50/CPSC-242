####################################################
# Homework 2 Problem 1
# author: Craig Shaffer
# date revision: 1/28/21
# course: CPSC 242
#
# creating a class for complex numbers. The class
# contains functions to compare, add, subtract, 
# multiply and divide. The functions take two 
# complex numbers and return the result for the 
# operation
#
####################################################

# Clarification:
# prior to this assignment I knew that j represents complex numbers instead of 
# i for python. I do not know if j counts as a prewritten function or not. If it
# does, I can rewrite this code for you with out the use of it.

# creates class for the complex number
class complex_num:
    
    #constuctor function
    def __init__(self, real, imag=None): #giving imag none type allows it to still be
                                         #imaginary if the user does not give imag a value
        self.real = real
        self.imag = imag
        print(self.real + self.imag)
   
    #function to compare two complex numbers
    def compare(self, other):
        #if both real numbers are equal and both imaginary numbers are equal, they are equal
        if (self.real==other.real and self.imag==other.imag):
            print("The complex numbers are equal")
        else:
            print("The complex Numbers are not equal")
    
    #function to add two complex numbers to get the sum
    def get_sum(self, other):
        print("The sum is: ")
        return complex_num(self.real + other.real, self.imag + other.imag)
        #adds the reals together and imaginaries together separately
    
    #function to subtract one complex number from another to get the difference
    def get_diff(self, other):
        print("The difference is: ")
        return complex_num(self.real - other.real, self.imag - other.imag)
        #subtracts the real from real and imaginary from imaginary separately
    
    #function to multiply two complex numbers to get the product
    def get_prod(self, other):
        print("The product is: ")
        return complex_num((self.real * other.real) + (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))
            #this function is based on: (a+bi)(c+di)=(ac)+(ad)i+(bc)i+(bi*di)
    
    #function to divide one complex number from another to get the quotient
    def get_quot(self, other):
        print("The quotient is: ")
        divisor = ((other.real)**2 + (other.imag/1j)**2)
        #the divisor is calculated by using the values of the second complex
        #number, squaring them, and then adding them together
        
        return complex_num(((self.real * other.real) -
        (self.imag * other.imag))/divisor,
        (((((self.imag)/1j) * other.real) - (self.real * (other.imag)/1j))*1j)/divisor)
        #this function is based on:
        #(a+bi)/(c+di)=(ac-bi*di)/divisor + ((b*c)-(a*d)i)/divisor
    
#Testing all functions within the class
###################################################

#two test complex numbers
c1 = complex_num(12,3j) #(a+bi)
c2 = complex_num(9,7j) #(c+di)

#function calls from the class
c1.get_sum(c2) #addition
c1.get_diff(c2) #subtraction
c1.get_prod(c2) #multiplication
c1.get_quot(c2) #division
c1.compare(c2) #equivilence
