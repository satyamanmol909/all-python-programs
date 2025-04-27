import random

real_random=0
real_random=random.randint(1,100)
while(True):
    num=int(input("Guess the number between :"))
    if num>real_random:
        print("number is too big:")
    elif num<real_random:
        print("number is too small")
    else:
        break
