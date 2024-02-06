import random
import subprocess as sub

maxNumber = 100
lowestNumber = 1
guesses = 0

def user_choice(text):
    global guesses
    try:
        userChoice = input(text)
        if userChoice == "/exit":
            return userChoice
        else:
            guesses += 1
            return int(userChoice)
    except:
            print("⚠️  Not a valid entry")  

def setup():
    botChoice = random.randint(lowestNumber, maxNumber)
    userChoice = user_choice("Pick a random number between 1-100! -   ")
    return botChoice, userChoice

def main(botChoice, userChoice):
    global guesses
    while 1:  
        if userChoice == botChoice:
            print(f"✓   -   {guesses} guesses!")
            guesses = 0
            userChoice = user_choice("New game [1: Yes | 0: No] -   ")
            if userChoice:
                botChoice = random.randint(lowestNumber, maxNumber)
                userChoice = user_choice("Pick a random number between 1-100! -   ")
            else:
                break
        elif userChoice > botChoice:
            userChoice = user_choice("Pick ↓ -   ")
        elif userChoice < botChoice:
            userChoice = user_choice("Pick ↑ -   ")
        elif userChoice == "/exit":
            break

botChoice, userChoice = setup()
main(botChoice, userChoice)