# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:06:17 2021

@author: craig
"""
#template
class human:
    #data for human class:
        #name
        #age
        #weight
        #height
    
    #construsctor function
    def __init__(self, name1, age1, weight1, height1):
        self.name = name1
        self.age = age1
        self.weight = weight1
        self.height = height1
    
    def print_human(self):
        print('name: ', self.name)
        print('age: ', self.age)
        print('weight:', self.weight)
        print('height: ', self.height)
        
    def compare_age(self, otherHuman):
        if (self.age == otherHuman.age):
            print(self.name, "and", otherHuman.name, "are the same age")
            
#instantiation or instance on object

human1 = human('harry potter', 7, 55, 3)

human1.print_human()

human2 = human('harry potter', 7, 55, 3)

human2.print_human()

human3 = human('hue janus', 7, 40, 4)

human3.print_human()

human1.compare_age(human3)




