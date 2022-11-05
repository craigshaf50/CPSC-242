# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:08:52 2021

@author: swamy
"""

from stack import Stack
from tree import BinaryTree

def evaltree(ptree):
   
   if(type(ptree.root) == int):
      return ptree.root
      
   elif(ptree.root == '+' ):
      x = evaltree(ptree.left_child) + evaltree(ptree.right_child)
      ptree.root = x
      return x
   elif(ptree.root == '*' ):
      x = evaltree(ptree.left_child) * evaltree(ptree.right_child)
      ptree.root = x
      return x
   elif(ptree.root == '-' ):
      x = evaltree(ptree.left_child) - evaltree(ptree.right_child)
      ptree.root = x
      return x
   elif(ptree.root == '/' ):
      x = evaltree(ptree.left_child) / evaltree(ptree.right_child)
      ptree.root = int(x)
      return int(x)
   
   
def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
       
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child

        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child

        elif i == ")":
            current_tree = p_stack.pop()

        elif i not in ["+", "-", "*", "/", ")"]:
    
                current_tree.root = int(i)
                parent = p_stack.pop()
                current_tree = parent

    print(evaltree(expr_tree))
     
    return expr_tree


pt = build_parse_tree("( ( 10 * 5 ) + ( 3 / 2 ) )")
#pt.postorder()  # defined and explained in the next section
