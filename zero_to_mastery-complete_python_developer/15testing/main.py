import random

answer = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess the number between 1 and 10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius!")
                break
        else:
            print("Hey man, I said 1~10")

    except ValueError:
        print("Please enter a number")
        continue
