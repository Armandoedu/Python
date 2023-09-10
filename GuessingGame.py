import random
import os

fail=0
luck=random.randrange(0,100)

player=int(input("Try to guess a number from 0 to 100: "))

while luck!=player:
    os.system('cls')
    if luck>player:
        print("\t\tWRONG\ntry a bigger number")
    elif luck<player:
        print("\t\tWRONG\ntry a smaller number")
    fail +=1
    player=int(input("Try to guess a number from 0 to 100: "))
print("\t\tCongratulations!!\n\t\tYou`re right\nYou made mistake ", fail, "times")
