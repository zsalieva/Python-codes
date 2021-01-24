
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

operation= input("Enter your operation ")

# main function
def main(operation, number1, number2):
    if operation=="addition":
        addition(number1,number2)
    elif operation=="subtraction":
        subtraction(number1, number2)
    elif operation=="division":
        division(number1, number2)
    elif operation=="multiplication":
        multiplication(number1, number2)
    else:
        print("invalid mathematical operation")
# 1st function: addition
def addition(n1,n2):
    print(n1+n2)
    return(n1+n2)
# 2nd function: subtraction
def subtraction(n1,n2):
    print(n1-n2)
    return(n1-n2)
# 3rd function: division
def division(n1,n2):
    print(n1/n2)
    return(n1/n2)
# 4th function: multiplication
def multiplication(n1,n2):
    print(n1*n2)
    return(n1*n2)
main(operation, 15, 25)
