import random

score = 10

while True:
    user = input("Higher or lower than 0? -> ")
    number = random.randint(1,10) * random.choice([-1,1])
    if number < 0 and user == "l":
        print("winner!", number)
        score += 1
    if number < 0 and user == "h":
        print("loser!", number)
        if score > 0:
            score -= 1
    if number > 0 and user == "l":
        print("loser!", number)
        if score > 0:
            score -= 1
    if number > 0 and user == "h":
        print("winner!", number)
        score += 1
    print(f"The score is: {score}")
    loop = input("Again? y/n -> ")
    if loop == "n":
        break
