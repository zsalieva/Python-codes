#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

i=0
while i < 6:
    i+=1
    if i == 6:
        print("You have been kicked out of system.")
        break
    passw = input("Please enter your password: ")
    if passw == "password":
        print("Welcome to system.")
        break
    else:
        print("Wrong password. Try again.")