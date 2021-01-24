
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# continue statement is used to skip that iteration and continue to the next one in the loop
fruits = ["apple", "banana", "cherry", "orange", "pear", "banana"]
otherList = []
for x in fruits:
  if x == "banana":
    otherList.append(x)
    continue
  print(x)
print(otherList)

#---------------------------
# break: breaks the loop

fruitss = ["apple", "banana", "cherry", "orange", "pear", "banana"]
otherList = []
for x in fruitss:
  if x == "banana":
    break
  print(x)

  
