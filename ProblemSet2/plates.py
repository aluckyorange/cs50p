def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    
    first_number = ""
    for ch in s:
        if not ch.isdigit() and not ch.isalpha():
            return False
        if len(first_number) != 0 and ch.isalpha():
            return False
        if len(first_number) == 0 and ch.isdigit():
            if ch == "0":
                return False
            first_number = ch
    
    return True

main()