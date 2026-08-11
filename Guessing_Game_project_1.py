import random
rn = random.randint(1,10)
g = int(input("guess: "))
while g != rn:
    if g > rn:
        print("lower")
    elif g < rn:
        print("higher")
    g = int(input("again?: "))
print("correct its",rn,"you win.")