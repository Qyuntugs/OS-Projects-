slot1 = int(input("slot1: "))
operation = input("opera: ")
slot2 = int(input("slot2: "))
if operation == "+":
    print("result:",slot1 + slot2)
elif operation == "-":
    print("result:",slot1 - slot2)
elif operation == "*":
    print("result:",slot1 * slot2)
elif operation == "/":
    print("result:",slot1 / slot2)
ac = input("more calculation?: ")
while bool(ac) == True:
    slot1 = int(input("slot1: "))
    operation = input("opera: ")
    slot2 = int(input("slot2: "))
    if operation == "+":
        print("result:",slot1 + slot2)
    elif operation == "-":
        print("result:",slot1 - slot2)
    elif operation == "*":
        print("result:",slot1 * slot2)
    elif operation == "/":
        print("result:",slot1 / slot2)
    ac = input("more calculation?: ")
print("done")