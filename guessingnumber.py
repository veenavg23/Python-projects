
# Guessing number


import random
import math
print("Welcome to number guessing game")
lb=int(input("Enter the lower bound: "))
ub=int(input("Enter the upper bound: "))
num=random.randint(lb,ub)
chances=math.log((ub-lb)+1,2)
print("\n\tYou've only",round(chances),"chances to guess the integer\n")
round1=0
while round1<chances:
    round1+=1 
    print("\tNo.of chances: ",round1,"Guess a number:",end="")
    guess=int(input())
    if guess>num:
        print("Try Again! You guessed too high")
    elif guess<num:
        print("Try Again! You guessed too small")
    elif guess==num:
        print("Congratulations!,you did it in ",round1,"try")
    else:
        print("Better Luck Next Time!")
      

