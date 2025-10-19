while True:
    x, y = input("Fraction: ").split("/")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        continue
    try:
        percent = round(x / y * 100)
    except ZeroDivisionError:
        continue
    if percent > 100:
        continue

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

