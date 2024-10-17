# name = ""
# while name != "your name":
#     print("Please type your name.")
#     name = input()
# print("Thanks!")

# while True:
#     print("Please type your name.")
#     name = input()
#     if name == 'your name':
#         break
# print("Tanks")

# import random
# for i in range(5):
#     print(random.randint(1,10))

import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20")
for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print("You is so amazing and incredibles. It took you " + str(guessesTaken) + " guesses!")
else:
    print("You ran out of guesses. I was thinking of " + str(secretNumber))