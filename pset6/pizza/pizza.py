import sys
import csv
from tabulate import tabulate


def main():
    if valid() is True:
        try:
            with open(sys.argv[1]) as csvfile:
                reader = csv.reader(csvfile)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File doesn't exist!")


def valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") is True and len(sys.argv) == 2:
        return True
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
