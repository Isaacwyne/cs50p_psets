import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    match = re.findall(r"(\bum\b)", s, flags=re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()
