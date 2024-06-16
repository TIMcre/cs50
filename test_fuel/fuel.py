def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    gauge_level = gauge(percentage)
    print(gauge_level)


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
