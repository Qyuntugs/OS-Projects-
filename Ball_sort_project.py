import random
ball_generate = int(input("How Many Balls To Generate?: "))
red = 0
green = 0
blue = 0
for _ in range(ball_generate):
    ball = random.choice(["Red Ball","Green Ball","Blue Ball"])
    if ball == "Red Ball":
        red += 1
    elif ball == "Green Ball":
        green += 1
    elif ball == "Blue Ball":
        blue += 1
print(f"{red}x Red Ball")
print(f"{green}x Green Ball")
print(f"{blue}x Blue Ball")