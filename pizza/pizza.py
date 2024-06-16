from tabulate import tabulate
import csv
import sys


def open_file(input_file):
    output = []
    try:
        with open(input_file) as file:
            reader = csv.reader(file)
            for row in reader:
                output.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return output


def check_length():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def main():
    check_length()
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    file = open_file(sys.argv[1])
    print(tabulate(file[1::], tablefmt="grid", headers=file[0]))


if __name__ == "__main__":
    main()
