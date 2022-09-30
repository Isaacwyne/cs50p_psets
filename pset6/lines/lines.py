import sys


def main():
    if valid() is True:
        try:
            print(evaluate())
        except FileNotFoundError:
            sys.exit("File doesn't exist!")


# check
    # if the command-line argument is a Python file
    # if a command-line argument is provided
def valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") is True and len(sys.argv) == 2:
        return True
    else:
        sys.exit("Not a Python file")


def evaluate():
    count = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if not line.strip().startswith("# ") and line.strip() != "":
                count += 1
    return count


if __name__ == "__main__":
    main()
