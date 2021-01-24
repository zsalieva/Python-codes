

#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

#1st Function returns are of rectangle. 
#2nd fuunction calculates volume of a regtangular prisim using the return value from the 1st fuunction
#Regtangular prisim, l,h,w,
#volume = l * W * H
#baseArea= l * w
#volume=baseArea*h

def area(length, width):
    baseArea = length * width
    print("base area = ", baseArea)
    return(baseArea) # helps to use the baseArea in another function

#area(15, 10)

def  volumeValue(baseArea, height):
    volume=baseArea*height
    print("volume = ", volume)
volumeValue(area(30,10), 10)
#-------------

# rectangular prism, length, width, height 
# volume = l * w * h
# baseArea = l * w 
# volume = baseArea * h
#1st function  calculate base area
def area(length, width):
    baseArea = length * width
    print("base area = ", baseArea)
    return(baseArea)
base2 = area(15,10)
#2nd option
print("base area outside: ", base2)
# 1st 
print("base area outside: ", area(15,10))