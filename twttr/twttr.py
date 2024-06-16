def removechars(text, blacklist):
    returntext = []
    for char in text:
        if char.lower() not in blacklist:
            returntext.append(char)
    return "".join(returntext)


inputtext = input("Input: ")
outputtext = removechars(inputtext, blacklist=["a", "e", "i", "o", "u"])
print(f"Output: {outputtext}")
