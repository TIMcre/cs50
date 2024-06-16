def main():
    outputtext = shorten(input("Input: "))
    print(f"Output: {outputtext}")


def shorten(word):
    returntext = []
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            returntext.append(char)
    return "".join(returntext)


if __name__ == "__main__":
    main()
