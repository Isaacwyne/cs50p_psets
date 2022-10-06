import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"((?:[0-9][0-2]?)(?:\:[00-59]+)?(?: AM|PM)) to ((?:[0-9][0-2]?)(?:\:[00-59]+)?(?: AM|PM))$",
                         s, flags=re.ASCII):
        return f"{time.group(1)} - {time.group(2)}"
    else:
        raise ValueError("Invalid format")


if __name__ == "__main__":
    main()
