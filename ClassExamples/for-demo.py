# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:12:13 2021

@author: swamy ponpandi

iterating through sequences using for loop

sets, lists, strings, tuple, dictionary

"""

#lists
list1 = ['cat', 'mouse', 'lion', 'dog']

for item in list1:
   print(item)
   
#sets 

set1 = {'cat', 'mouse', 'lion', 'dog', 'dog'}

for item in set1:
    print(item)

#tuples

# tuple1 = ('homer', 34, '999-00-1234')

# for item in tuple1:
#    print(item)

states_capitals = { "ia" : "des moines",
                     "co" : "denver",
                     "il" : "springfield",
                     }

for state in states_capitals:
    print(state, " : ", states_capitals[state])
    
    