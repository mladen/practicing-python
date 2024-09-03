import random


def is_guess_in_range(guess: int) -> bool:
    """
    Check whether the guess is within the range of 1 and 10.

    :param guess: an integer representing the guessed number
    :return: a boolean indicating whether the guess is within range
    """
    return isinstance(guess, int) and 1 <= guess <= 10


# -def is_guess_in_range(guessedNumber: int):
# -    if type(guessedNumber) != int:
# -        return False
# -    return 1 <= guessedNumber <= 10


def is_exact_number(guess: int, answer: int) -> bool:
    return (
        guess == answer if isinstance(guess, int) and isinstance(answer, int) else False
    )


# -def is_exact_number(guess: int, answer: int):
# -    return guess == answer


def game():
    while True:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
            if is_guess_in_range(guess):
                if is_exact_number(guess, answer):
                    print("You got it!")
                    break
            else:
                print("Hey man, I said 1~10")

        except ValueError:
            print("Please enter a number")
            continue


if __name__ == "__main__":
    answer = random.randint(1, 10)
    game(answer)
