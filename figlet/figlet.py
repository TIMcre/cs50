from pyfiglet import Figlet as figlet
import sys
import random


def check_argv(arg=sys.argv):
    if len(arg) not in (3, 1):
        sys.exit("Invalid Usage")
    if len(arg) == 3 and arg[2] in figlet.getFonts() and arg[1] in ("-f", "--font"):
        figlet.setFont(font=arg[2])
    elif len(arg) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        sys.exit("Invalid Usage 1")


if __name__ == "__main__":
    figlet = figlet()
    check_argv()
    text = input("Input: ")
    print(f"Output:\n{figlet.renderText(text)}")
