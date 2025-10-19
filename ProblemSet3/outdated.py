months_list = [
    "None",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def check_date(y, m, d):
    if m < 1 or m > 12:
        return False
    if m != "2" or not is_leap_year(y):
        return d <= days_list[m]
    return d <= 29


while True:
    date = input("Date: ")
    if "/" in date:
        mon, day, year = date.split("/")
        mon = int(mon)
        day = int(day)
        year = int(year)
    elif date.split()[0] in months_list:
        mon =int(months_list.index(date.split()[0]))
        day = int(date.split()[1][:-1])
        year = int(date.split()[2])
    else:
        continue
    if check_date(year, mon, day):
        print(f"{year:04}-{mon:02}-{day:02}")
        break