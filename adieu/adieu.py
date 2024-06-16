def adieu_to(names):
    match len(names):
        case 1:
            print(f"Adieu, adieu, to {names[0]}")
        case 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
        case _:
            print("Adieu, adieu, to ", end="")
            for name in names:
                if name is names[-1] and len(names) > 2:
                    print(f"and {name}")
                else:
                    print(name, end=", ")


names = []
while True:
    try:
        name = input()
        names.append(name)

    except EOFError:
        break

adieu_to(names)
