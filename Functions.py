#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Write a program that has two different functions.
# First function asks for user input for cylinder height and radius.
# First function should pass height and radius values onto the Second function
# which calculates the volume of the cylinder.  

def volume_cylinder(radius,height):
    area = area_circle(radius)
    return area * height
def area_and_volume(radius, height):
    #print "For a cylinder with radius", radius, "and height", height
  #  print "The surface area is", area_cylinder(radius,height)
    print ("The volume is", volume_cylinder(radius,height))  

volume_cylinder(radius,height)
area_and_volume  