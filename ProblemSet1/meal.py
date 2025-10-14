def main():
    time_val = convert(input("What time is it? "))
    if convert("7:00") <= time_val <= convert("8:00"):
        print("breakfast time")
    elif convert("12:00") <= time_val <= convert("13:00"):
        print("lunch time")
    elif convert("18:00") <= time_val <= convert("19:00"):
        print("dinner time")

def convert(time: str):
    time_val = 0
    if time.endswith(" a.m."):
        time = time.replace(" a.m.", "")
    elif time.endswith(" p.m."):
        time_val += 12
        time = time.replace(" p.m.", "")
    hour, minute = time.split(":")
    time_val += float(hour) + float(minute) / 60
    return time_val

if __name__ == "__main__":
    main()