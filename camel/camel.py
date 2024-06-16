camelCase = input("camelCase: ")
snake_case = []

for char in camelCase:
    if char.isupper():
        snake_case.append("_")
    snake_case.append(char.lower())

print("".join(snake_case))
