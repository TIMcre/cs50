import sys
import re


def check_length():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def open_file(input_file):
    try:
        with open(input_file) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines


def is_empty(line):
    line = line.strip()
    return line == "" or line.startswith(
        "#"
    )  # or re.match(r"^\s*[\'\"]{3}[^\'\"]*[\'\"]{3}\s*$", line.strip())


def is_docstring(line):
    if (
        line.strip().endswith('"""')
        or line.strip().endswith("'''")
        or line.strip().startswith('"""')
        or line.strip().startswith("'''")
    ):
        return True
    return False


def amount_lines(lines):
    count = 0
    # in_docstring = False
    # docstring_status = False
    for line in lines:
        # not is_empty(line) and not in_docstring:
        # docstring_status = is_docstring(line)
        if not is_empty(line):  # and not docstring_status and not in_docstring:
            count += 1

        # elif docstring_status:
        # in_docstring = not in_docstring

    return count


def main():
    check_length()

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    file = open_file(sys.argv[1])
    amount = amount_lines(file)

    print(amount)


if __name__ == "__main__":
    main()


# I found it quite hard to understand what should be countet as lines of code cause this doesnt make sense to me as real code. please help me understand waht is code in your eyes
