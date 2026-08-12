import time
import random
print("console log:")
for r in range(5):
    l = random.choice(["waiting for network connection...","connection to database is required."])
    rdl = random.randint(2,7)
    for lt in range(rdl):
        time.sleep(0.1)
        print(".")
    print(l)
o = random.choices(
    ["Sucsessfully connected to database.","failed to connect..."],
    weights=[30,70])
print(o)