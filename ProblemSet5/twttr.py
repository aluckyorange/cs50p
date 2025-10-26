def main():
    word = input("Input word: ")
    print("Output:", shorten(word))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", 
              "a", "e", "i", "o", "u"]
    for ch in word:
        if ch in vowels:
            word = word.replace(ch, "")
    return word


if __name__ == "__main__":
    main()