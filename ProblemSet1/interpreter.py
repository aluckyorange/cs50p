expression = input("Expression: ")

x = float(expression.split(" ")[0])
op = expression.split(" ")[1]
y = float(expression.split(" ")[2])

match op:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
    case _:
        print(f"Invalid op: {op}")