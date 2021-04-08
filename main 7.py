# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#song guessing game

song = {
    "name" : "vilambara idaivelai",
    "artist": "hiphop tamizhan",
    "album": "imaika nodigal",
    "recorded": 2017,
    "released": 2018,
    "duration": 4.25,
    "genre": "love",
    "label": "barathiyar"
}
def SongGame():
    print("\n****SongGame****")
    for key in song :
        print(key,":",song[key])
    print("\n****end****")  
    
def AskQuestion():
    key = input("\nGreat,let's start the game,guess the key?\n")
    value = input("\nWhat you think is the value of " + key + "?\n")
    if key and value :
        key = key.lower()
        value = value.lower()
        if key in song and song[key].lower() == value :
           return True
    return False

def startGuessingGame():
    if AskQuestion():
        print("Bingo! You guessed it right...")
    else:
        print("Oops... You missed!")
        repeat = input("\nWant try again? Say 'yes' to continue or say 'no'.\n")
        if repeat == "yes":
            startGuessingGame()
        else:
            print("\nSee you again!")

SongGame()

print("start game")

startGuessingGame()    

