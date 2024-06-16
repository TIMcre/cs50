expression = input("Expression: ").split(" ")
match expression[1]:
    case "+":
        print(round(float(expression[0]) + float(expression[2]), 1))
    case "-":
        print(round(float(expression[0]) - float(expression[2]), 1))
    case "/":
        print(round(float(expression[0]) / float(expression[2]), 1))
    case "*":
        print(round(float(expression[0]) * float(expression[2]), 1))
