while True:
    try:
        x, y = input("Fraction: ").split("/")
        percentage = round((int(x) / int(y)) * 100)

        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        elif percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break

    except:
        pass
