import inflect

p = inflect.engine()

name_list = []
while True:
    try:
        name_list.append(input("Name: "))
    except EOFError:
        break

print()
print("Adieu, adieu, to " + p.join(name_list, final_sep=""))