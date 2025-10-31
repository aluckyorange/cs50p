import sys
import csv


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()
if not sys.argv[1].rstrip().endswith(".csv"):
    print("Not a CSV file")
    sys.exit()
try:
    in_file = open(sys.argv[1])
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit()

with open(sys.argv[2], "w") as out_file:
    reader = csv.DictReader(in_file)
    writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in reader:
        writer.writerow({
            "first": row["name"].split(",")[0].strip(), 
            "last": row["name"].split(",")[1].strip(),
            "house": row["house"]
        })

in_file.close()