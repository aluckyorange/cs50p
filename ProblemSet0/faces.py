def convert(content: str):
    return content.replace(":)", "🙂").replace(":(", "🙁")


def main():
    content = input("Please input something: ")
    print(convert(content))


main()