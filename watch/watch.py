import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(
        r"(src=\")(https?://)(www.)?(youtube\.com)(/embed/)(.{11})\"", s
    ):
        return f"https://youtu.be/{match.groups()[-1]}"
    return None


if __name__ == "__main__":
    main()
