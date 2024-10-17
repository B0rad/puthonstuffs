# def spam():
#     eggs="spam local"
#     print(eggs) #Prints spam localblo
# def bacon():
#     eggs = "bacon local"
#     print(eggs)
# spam()
# eggs = "global"
# bacon()
# print(eggs)

def spam():
    global eggs
    eggs = "spam"
    eggs = 'global'
spam()
print(eggs)
