import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if re.match(r"^(?=.{2,6}$)[A-Z]{2,}(?!0\d*)\d*$", s):
        return True
    return False


if __name__ == "__main__":
    main()
