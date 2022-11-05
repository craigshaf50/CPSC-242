# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:32:38 2021

@author: swamy
"""

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)
    
    def print_q(self):
       print(self._items)

# q = Queue()

# q.enqueue(2)
# q.enqueue('hello')
# q.enqueue(5.67)

# q.print_q()


