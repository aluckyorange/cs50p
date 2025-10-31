import sys
from tabulate import tabulate
import csv


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()
if not sys.argv[1].rstrip().endswith(".csv"):
    print("Not a CSV file")
    sys.exit()
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    print("File does not exist")
    sys.exit()

reader = csv.DictReader(file)
print(tabulate(reader, headers="keys", tablefmt="grid"))

file.close()