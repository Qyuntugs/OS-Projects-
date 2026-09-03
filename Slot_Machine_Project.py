import random
W = 0
L = 0
while True:
    slot_1 = random.choice(["R","G"])
    slot_2= random.choice(["R","G"])
    slot_3 = random.choice(["R","G"])
    print(slot_1,slot_2,slot_3)
    if slot_1 == "G" and slot_2 == "G" and slot_3 == "G":
        print("You Win")
        W+=1
    elif slot_1 != "G""R" and slot_2 != "G""R" and slot_3 != "G""R":
        L+=1
    print("You Lost",L,"Times")
    print("You Won",W,"Times")
    rr = input("Roll Again?: ")
    if rr.lower() == "no":
        break