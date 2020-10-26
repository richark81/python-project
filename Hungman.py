# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

def hungman():
    word=random.choice(["pugger","littlepugger","hello", "avengers","pokemon","thor","earth"])
    print(word)
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ""
    while len(word)>0:
        main=""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win")
            break
        
        print("Guess the word:", main)
        guess= input()
        
        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
            
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print(" --------- ")
            if turns == 8:
                print("8 turns left")
                print(" --------- ")
                print("     O     ")
            if turns == 7:
                print("7 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
            if turns == 6:
                print("6 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
                print("    /      ")
            if turns == 5:
                print("5 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
                print("    / \     ")
                
            if turns == 4:
                print("4 turns left")
                print(" --------- ")
                print("   \ O     ")
                print("     |     ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print(" --------- ")
                print("   \ O /    ")
                print("     |     ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print(" --------- ")
                print("   \ O /|   ")
                print("     |     ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print(" --------- ")
                print("   \ O_|/   ")
                print("     |     ")
                print("    / \     ")
            if turns == 0:
                print("you loose..!! you let kind man die")
                print(" --------- ")
                print("     O_|/   ")
                print("    /|\     ")
                print("    / \     ")
                break
    
    
    
name=input("ent the name")
print("Welcome",name)
print("-----------------")
print("try to guess the word in less than 10 attemps")
hungman()
print()

