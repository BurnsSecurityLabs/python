import random, sys


lettersList=["r","p","s"]
print("ROCK, PAPER, SCISSORS")
computer1 =random.choice(lettersList)

#variables to keep track of ongoing scores
wins = 0
losses = 0
ties = 0
 
while True: #main game loop
    print ('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #human1 input loop
        computer1 =random.choice(lettersList)
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
        human1 = input()
        if human1 == 'q':
            print("Thanks for playing!")
            sys.exit() # ends game and program

        if human1 == 'p' or human1 == 'r' or human1 == 's' or human1 == 'q':
            break
            print("Type p, r, s, or q.")

    #human choice
    if human1 == 'r':
        print("ROCK versus...")
    elif human1 == 'p':
        print("PAPER versus...")
    elif human1 == 's':
        print("SCISSOR versus...")

    #computer choice
    if computer1 == 'r':
        print("ROCK")
    elif computer1 == 'p':
        print('PAPER')
    elif computer1 == 's':
        print('SCISSOR')
        
    #paper beats rock
    #while human1 ="q":
    if (human1 == computer1):
        print ("Its a tie!")
        ties +=1
    #rock vs paper - lose
    if human1 == "r" and computer1 == 'p':
        print("You lose!")
        losses +=1
    #paper vs scissor - lose
    elif human1 == "p" and computer1 == 's':    
        print("You lose!")
        losses +=1
    #scissor vs rock -- lose
    elif human1 == "s" and computer1 == 'r': 
        print("You lose!")
        losses +=1
    #rock vs scissor -- win
    elif human1 == "r" and computer1 == "s":
        print("You win!")
        wins +=1
    elif human1 == "s" and computer1 == "p":
        print("You win!")
        wins +=1
    elif human1 == "p" and computer1 == "r":
        print("You win!")
        wins +=1




