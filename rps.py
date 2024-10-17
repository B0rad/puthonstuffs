import random, sys
print("Rock, Paper, Scissors!")

#Vars to keep track of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:     #Main game loop
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True: #player input loop
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit() #Quits the game (sysexit)
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break #break out of the loop
        print("Type one of r, p, s, or q.")

    #display what the player chose
    if playerMove == "r":
        print("ROCK vs...")
    elif playerMove == "p":
        print("PAPER vs...")
    elif playerMove == "s":
        print("SCISSORS vs...")

    #display what computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK!")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER!")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS!")
    
 #Display and record win/loss/tie

    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print('You win!')
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("You LOSE!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("You LOSE!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("You LOSE!")
        losses = losses + 1