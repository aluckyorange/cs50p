def main():
    plate = input("Plate: ")
    print("Valid:", is_valid(plate))


def is_valid(s:str):
    if len(s) < 2 or len(s) > 6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    sep_idx = 0
    while sep_idx < len(s):
        if s[sep_idx].isdigit():
            break
        sep_idx += 1
    
    if sep_idx < len(s) and s[sep_idx] == "0":
        return False
    for ch in s[sep_idx:]:
        if not ch.isdigit():
            return False
        
    return True


if __name__ == "__main__":
    main()