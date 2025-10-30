import sys


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()
if not sys.argv[1].rstrip().endswith(".py"):
    print("Not a Python file")
    sys.exit()

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    print("File does not exist")
    sys.exit()

loc = 0
for line in file:
    line = line.lstrip()
    if not (line == "" or line.startswith("#")):
        loc += 1

print(loc)
file.close()