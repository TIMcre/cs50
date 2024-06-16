c = 300000000


def main():
    m = get_int("m: ")
    E = m * c**2
    print(f"E:{E}")


def get_int(prompt="Integer:"):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("please input an integer")


if __name__ == "__main__":
    main()
