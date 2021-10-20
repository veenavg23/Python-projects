print("GUESSING WORD GAME")
name=input("What is your name: ")
print("Good Luck !",name)
import random
words=["passion","dreamjob","mlengineer","datascience"]
word=random.choice(words)
chances=(len(word))-1
print("your total no.of chances=",chances)
print(word)
print("_"*len(word))
wrd="_"*len(word)
while chances!=0:
    char=input("Guess the characters: ")
    if char in word:
        for i in range(len(word)):
            if char==word[i]:
                wrd=wrd[0:i]+char+wrd[i+1:]
        print(wrd)
        if wrd == word:
            print("You win")
            print("The word is , ", wrd)
            break
    else:
        chances-=1
        print("wrong\n You have",round(chances),"more guesses")
else:
    print("Better Luck next time")


