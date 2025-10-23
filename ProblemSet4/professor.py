import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for _ in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if ans == x + y:
                    score += 1
                    break
                print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in [1, 2, 3]:
            return level


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    number = random.randint(1, 9)
    for _ in range(level - 1):
        number *= 10 + random.randint(0, 9)
    return number


if __name__ == "__main__":
    main()