# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:12:02 2021

@author: swamy
"""

from myqueue import Queue

def hot_potato(name_list, num):
      sim_queue = Queue()
    
      for name in name_list:
       sim_queue.enqueue(name)

      sim_queue.print_q()
      
      while sim_queue.size() > 1:
          for i in range(num):
              x = sim_queue.dequeue()
              sim_queue.enqueue(x)
              sim_queue.print_q()
              
          sim_queue.dequeue()

      return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
