import random


money = 1
while True:
    print(f"You have {money} $")
    user = input("Higher or lower than 0? -> ")
    number = random.randint(1,10) * random.choice([-1,1])
    if number < 0 and user == "l":
        print("winner!", number)
        money += 1
    if number < 0 and user == "h":
        print("loser!", number)
        money -= 1
    if number > 0 and user == "l":
        print("loser!", number)
        money -= 1
    if number > 0 and user == "h":
        print("winner!", number)
        money += 1
    print(f"The money is: {money}")
    loop = input("Again? y/n -> ")
    if loop == "n":
        break
