import random


while True:
    user = input("Higher or lower than 0? -> ")
    number = random.randint(1,10) * random.choice([-1,1])
    if number < 0 and user == "lower":
        print("winner!", number)
    if number < 0 and user == "higher":
        print("loser!", number)
    if number > 0 and user == "lower":
        print("loser!", number)
    if number > 0 and user == "higher":
        print("winner!", number)
    loop = input("Again? Yes/No -> ")
    if loop == "no":
        break
