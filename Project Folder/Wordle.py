import random
import urllib.request as urllib2
from colorama import Fore

print('Your goal is to guess the word correctly!\n')
print('Green means: The letter is in the word AND in the right place\nYellow means: The letter is in the word BUT in the wrong place\nRed means: The letter is not in the word\n')
print('Note: If the word has multiple occurences of a letter, and your guess has more of those letters, the remainder will appear in RED instead of GREEN or YELLOW.\n')
print("Good Luck!\n")
print('\n--------------\n')

wordLength = 5

API = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
API_Response = urllib2.urlopen(API)
txt = API_Response.read().decode("utf-8").split() # decoding the bytes to use them as a string then separating the string using split
wordList = list(filter(lambda x: len(x) == wordLength, txt)) # making a list with only words of the specified length
wordToGuess = (random.choice(wordList)) # choosing a random word from the list

tries = 5
tleft = tries

while tleft > 0:

    while True:
        print(Fore.WHITE)
        if tleft < tries:
            if tleft < 2:
                print(f'You have {tleft} try left.\n')
            else:
                print(f'You have {tleft} tries left.\n')

        player = input("Guess: ")

        if len(player) == wordLength and player.isalpha() and player in wordList:
            break
        elif player not in txt:
            print(Fore.RED, "\nThat isn't a valid word.")
        else:
            print(Fore.RED, f'\nNeeds to be a {wordLength} letter word.')
    
    
    # Checking Answers
    green = []
    yellow = []
    red = []
    indices = []
    for i in range(wordLength):
        # if the letter isn't in the word, print red
        if player[i] not in wordToGuess:
            red.append(player[i])
            print(Fore.RED, player[i], end=" ")
            continue
            
        # if the letter is in the word and in the right place, print green
        if player[i] == wordToGuess[i]:
            green.append(player[i])
            print(Fore.GREEN, player[i], end=" ")
            continue
        # if the letter is in the word but is not in the right place, enter this condition    
        if player[i] in wordToGuess and player[i] != wordToGuess[i]:
            if (yellow.count(player[i]) + green.count(player[i])) >= wordToGuess.count(player[i]):
                # if there are too many occurences of the same letter, print red
                print(Fore.RED, player[i], end=" ")
                continue
            else:
                # print yellow if the letter is in the wrong place
                yellow.append(player[i])
                print(Fore.YELLOW, player[i], end=" ")
                continue
           
    print(Fore.WHITE)
    tleft = tleft - 1

    # Win Condition
    if player == wordToGuess:
        print("\nWell done.")
        break
    elif tleft <= 0: 
        print("\n" + f'You lost. The answer was "{wordToGuess}".')
