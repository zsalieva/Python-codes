#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# for x in range(2, 6):
#   print(x)   # output 2,3,4,5
#-----------------------------------
# adj = ["green", "yellow", "red","green", "yellow", "red","green", "yellow", "red","green", "yellow", "red","green", "yellow", "red"]

# print(len(adj))


#-----------------------------------
# for x in range(2, 30, 3):
#     #        start end increment   
#   print(x)



adj = ["green", "yellow", "red"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    
#output:
# ('green', 'apple')
# ('green', 'banana')
# ('green', 'cherry')
# ('yellow', 'apple')
# ('yellow', 'banana')
# ('yellow', 'cherry')
# ('red', 'apple')
# ('red', 'banana')
# ('red', 'cherry')


