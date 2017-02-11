import random
print ("for the organizer")
strike = int(input())
while True:
    print("enter a number between ",
        strike - random.randrange(1,20), " to ",
         strike + random.randrange(1,20))
    num = int(input())
    if num < strike:
        print("Too low")
        continue
    elif num > strike:
        print("Too high")
        continue
    else:
        print("correct number")
        break
