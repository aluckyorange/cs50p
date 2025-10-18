amount = 50

while True:
    print(f"Amount Due: {amount}")
    insert = int(input("Insert Coin: "))
    if insert not in [5, 10, 25]:
        continue
    amount -= insert
    if amount <= 0:
        break

print(f"Change Owed: {amount * -1}")
