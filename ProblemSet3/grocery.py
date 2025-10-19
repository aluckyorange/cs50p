grocery_dict = {}
grocery_list = []

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    if item not in grocery_dict:
        grocery_list.append(item)
        grocery_dict[item] = 0
    grocery_dict[item] += 1

grocery_list.sort()
for item in grocery_list:
    print(grocery_dict[item], item)
