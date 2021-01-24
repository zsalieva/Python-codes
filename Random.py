import os , sys
from _typeshed import SupportsReadline


# Lucky, extra lucky, not so lucky 
from random import randint
randomNumber = randint(6,16)
print(randomNumber)

# YOUR CODE GOES HERE:
# if randomNumber is equal to 7 then print you’re lucky
if  randomNumber==7 :
    print("Lucky")
# if randomNumber is equal 13 then print you’re unlucky
elif  randomNumber==13 :
    print("unLucky")
# randomNumber is equal to 5 and 15 then print you’re somewhat unlucky
elif  randomNumber==5 or  randomNumber==15 :
    print("You are somewhat Lucky")
else :
    print("Try again")

# everything else should be addressed with printing ‘try again’