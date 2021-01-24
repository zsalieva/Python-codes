#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Write a program that converts Celsius to Fahrenheit. 
# User should enter temperature in Celsius 
# and program should give it in Fahrenheit
# Formula: (°C * 1.8) + 32 = °F

Celsius=input("Enter Celsius to convert °C ")
C= int(Celsius)
num1=1.8
num2=32

Fahrenheit=(C* num1)+num2

print("Fahrenheit F= " , Fahrenheit)
