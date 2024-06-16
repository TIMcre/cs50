import random


def main():
    level = get_level()
    points = 0
    for _ in range(10):
        points = ask_question(level, points)
    print(f"Score: {points}")


def ask_question(level, points):
    x = generate_integer(level)
    y = generate_integer(level)
    for _ in range(3):
        print(f"{x} + {y} = ", end="")
        try:
            if x + y == int(input("")):
                points += 1
                return points
        except ValueError:
            pass
        print("EEE")
    print(f"{x} + {y} = {x+y}")
    return points


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except:
            pass


def generate_integer(level):
    level_ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    if level not in level_ranges:
        raise ValueError
    min_value, max_value = level_ranges[level]
    return random.randint(min_value, max_value)


if __name__ == "__main__":
    main()
