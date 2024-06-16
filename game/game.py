import random


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


while True:
    try:
        number = int(input("Level: "))
        if is_positive(number):
            number = random.randint(0, number)
            break
    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))
        if is_positive(guess):
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass

# no nice code at all
