def main():
    greeting = input("Greeting: ")
    print("Value:", value(greeting))


def value(greeting):
    if "hello" in greeting.lower():
        return 0
    elif "h" in greeting.lower():
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()