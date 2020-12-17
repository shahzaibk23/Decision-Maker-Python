import random
import sys
import os

if len(sys.argv) > 3:
    print("TOO MANY FLAGS")
    sys.exit()

if len(sys.argv) < 2:
    print("You need to specify, at least the choice flag !!")
    sys.exit()

if sys.argv[1] not in ["-c", "-C", "-r", "-R"]:
    print("Write Either -c for custom choice, or -r for random choice")
    sys.exit()
if len(sys.argv) == 3:
    if os.path.isfile(sys.argv[2]) == False:
        print("Path to file is not correct, or file does not exist")
        sys.exit()

if len(sys.argv) == 2:

    n = None
    lstOfThings = []
    print("Type the Tasks one after another, once you're done, type 'n' ")
    while n not in ["N","n"]:
        n = input("Enter: ")
        lstOfThings.append(n)

    lstOfThings=lstOfThings[:-1]
else:
    file = open(sys.argv[2])
    content = file.read()
    file.close()
    lstOfThings=content.split("\n")


random.shuffle(lstOfThings)

if sys.argv[1] in ["-c", "-C"]:
    index=int(input("ENTER NUMBER BETWEEN 1 to "+str(len(lstOfThings))+" : "))
    index -= 1
else:
    index = random.randrange(len(lstOfThings))

print("Decision made is: ",lstOfThings[index])





