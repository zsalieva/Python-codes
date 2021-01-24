
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys 
# i= 1

# while i < 6:
#   print(i)
#   i += 1

#--------------
# i= 10

# while i > 6:  # will infine printng and adding one 
#   print(i)
#   i += 1

#-------------
# break statement can stop the loop even if the while condition is true
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break     # 1,2,3 break
#   i += 1
# continue statement can stop the current iteration, and continue with the next
# i = 0
# newList=[]

# while i < 6:
#   i += 1
#   if i == 3:
#     newList.append(i)
#     continue
#   print(i)

#   print(newList)
#-----------------------

# temp = 0 
# #  != 
# while temp!=-999: 
#     temp = int(input('Enter a temperature (-1000 to quit): '))
#     fahrenheit =  (9/5*temp)+32
#     if temp==-999:
#         break
#     print('In Fahrenheit :', fahrenheit)

    
# how to avoid printing calculation of temp=-1000?

from random import randint
secret_num = randint(1,10)
guess = 0
while guess != secret_num:
    guess = int(input('Guess the secret number: '))
print('You finally got it!')
