import random
number = random.randint(1,100)
gnum = 0
while gnum != number:
    gnum = int(input("guess the number: "))
    if gnum > number:
        print('lower')
    elif gnum > number:
        print('higher')
    else:
        print('won')