#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Write a program that checks if any given number is divisible by 3 and 
# if it is divisible then it prints “fizz”.
# If number is divisible by 5 then it prints “buzz”. 
# And if it is divisible by both 5 and 3 then it should print “fizzbuzz”.


Number1 = input("Enter the  number ")
n1=int(Number1)
r= n1%3==0
r2=n1%5==0



if n1%3==0 and n1%5==0:
    print("FizzBuzz")  
if n1%3==0 and n1%5!=0 :
    print("Fizz")      
elif n1%5==0 and n1%3!=0:
    print("Buzz")  
   
       
