import random

min_value: int = 1
max_value: int = 10
answer = random.randint(min_value, max_value)


def guessedNumberInRange(min_value, max_value, guessedNumber: int):
    return min_value <= guessedNumber <= max_value


def exactNumber(guess: int, answer=answer):
    return guess == answer


def game():
    while True:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
            if guessedNumberInRange(min_value, max_value, guess):
                if exactNumber(guess):
                    print("You got it!")
                    break
            else:
                print("Hey man, I said 1~10")

        except ValueError:
            print("Please enter a number")
            continue


if __name__ == "__main__":
    game()
