import random, sys
#stores random number between 1-20
secretNum = random.randint(1,20)

#Output to screen for game
print("Hello, can you guess my security numer between 1-20?")
print("You have 6 chances")

#This sets the number of tries the users gets
for guessesTaken in range(1,7):
    print("take a guess:")
    #stores user's number
    yourGuess = int(input())

    # checks user number against computer random number
    if yourGuess != secretNum:
        print("Guess Again: ")
        # test statement: print("test: " + str(secretNum))
    else:
        
        break #happens only if user selects correct number


if yourGuess == secretNum:
    print("Congratulations! You guessd the correct number " + str(secretNum))
else:
    #user didn't guess correct number
    print('You lost')
    