def main():
    convertet_text = convert(input("text to be convertet:\n"))
    print(convertet_text)


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()
