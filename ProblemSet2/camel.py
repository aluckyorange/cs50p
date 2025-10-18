camel_case = input("camelCase: ")

snake_case = ""
for ch in camel_case:
    if ch >= "A" and ch <= "Z":
        snake_case += "_" + ch.lower()
    else:
        snake_case += ch

print(f"snake_case: {snake_case}")