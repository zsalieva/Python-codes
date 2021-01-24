
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys


#Write a program that multiplies all the items of a given list. All list items are integers.
total=1
Mylist =[2,3,4,5,6,7,8]

for i in range(0,len(Mylist)):
   total = total*Mylist[i]

print("The product of the all items in the list : ", total)