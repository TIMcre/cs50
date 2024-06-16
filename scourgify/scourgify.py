import csv
import sys


def open_file(input_file):
    output = []
    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                output.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    return output


def convert_data(data):
    new_data = []

    for entry in data:
        last, first = entry["name"].replace(" ", "").split(",")
        house = entry["house"]
        new_entry = {"first": first, "last": last, "house": house}
        new_data.append(new_entry)

    return new_data


def write_data(data, output_file):

    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def check_length():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def check_type(type):
    if not sys.argv[1].endswith(type):
        sys.exit(f"Not a {type.replace(".", "")} file")


def main():
    check_length()
    check_type(".csv")
    data = open_file(sys.argv[1])
    convertet_data = convert_data(data)
    write_data(convertet_data, sys.argv[2])


if __name__ == "__main__":
    main()
