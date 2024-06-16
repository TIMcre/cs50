import re
import sys


def main():
    if len(sys.argv) == 2:
        plate = sys.argv[1]
    else:
        plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if re.match(r"^(?=.{2,6}$)[A-Z]{2,}(?!0\d*)\d*$", s):
        return True
    return False


main()
