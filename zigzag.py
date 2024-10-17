import time, sys
indent=0
indentIncreasing = True

try:
    while True:
        print(' ' * indent,end="")
        print('*********')
        time.sleep(0.1) #pause for 1/10th of a second
        if indentIncreasing:
            #Increase indenting of spaces:
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False
        else:
            # Decrease spaces
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()