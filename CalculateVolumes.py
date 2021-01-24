#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Write a program that calculates volume of a cylinder.
# V=πr2h 5
pi=3.14
radius=input("Enter the Radius")
height=input("Enter the height")
r=int(radius)
h=int(height)
V= pi*r*2*h

print('The Volume of  given Cylinder equals ', V)
