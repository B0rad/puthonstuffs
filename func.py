# def Hello(name):
#     print("Howdy! " + name)
#     print()


# Hello("Bort")
# Hello("barry")
# Hello("Joey Joe Joe Shabbado")

# print(len("boobies"))

import random

# def getAnswer(answerNumber):
    
#     if answerNumber == 1:
#         return "It is certain"
#     elif answerNumber == 2:
#         return "It is decidely so"
#     elif answerNumber == 3:
#         return "Yesh"
#     elif answerNumber == 4:
#         return "Reply hazy, try again"
#     elif answerNumber == 5:
#         return "Aks again later"
#     elif answerNumber == 6:
#         return "Concentrate and ask again"
#     elif answerNumber == 7:
#         return "My reply is no"
#     elif answerNumber == 8:
#         return "Outlook is doubtfull"
#     elif answerNumber == 9:
#         return "Very doubtfull"
# print(getAnswer(random.randint(1,9)))


# print("i dont know what end does", end="smut")
# print("did it work?")
# print("cats","dags","meese",sep=",")
import random, sys

messages = ["It is certain", "It is decidedly so", "Yeah sure", "I dunno, ask again", "Aks again later", "Think more and ask again", "Nope", "I really don't think so"]

def magicEight():
    while True:
        print("Ask your question or type exit to quit")
        shakeBalls=input()
        if shakeBalls != "exit":
            print(messages[random.randint(0,9)])
            
        elif shakeBalls == "exit":
            sys.exit()

magicEight()