# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:17:59 2021

@author: swamy
"""

class Deque:
    """Deque implementation as a list"""

    def __init__(self):
        """Create new deque"""
        self._items = []

    def is_empty(self):
        """Check if the deque is empty"""
        return not bool(self._items)

    def add_front(self, item):
        """Add an item to the front of the deque"""
        self._items.append(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque"""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove an item from the front of the deque"""
        return self._items.pop()

    def remove_rear(self):
        """Remove an item from the rear of the deque"""
        return self._items.pop(0)

    def size(self):
        """Get the number of items in the deque"""
        return len(self._items)

    def print_deq(self):
       print(self._items)

# d = Deque()

# d.add_front(5)
# d.add_front(8)
# d.add_rear(4.4)
# d.add_rear(2.34)
# d.print_deq()
   