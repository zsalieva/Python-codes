
#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

from random import randint
secret_num = randint(1,100)
guess = 0
i=0
while i < 11:
    i+=1
    guess = int(input('Guess the secret number: '))
    if guess > secret_num:
        print("Your guess is higher than the number.")
    elif guess < secret_num:
        print("Your guess is lower than the number.")
    elif guess == secret_num:
        print("You finally got it!")
        break
    elif i == 10:
        print('You lost your 10 chances')

        