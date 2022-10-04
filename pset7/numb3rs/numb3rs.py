import re
import sys


def main():
    print(validate(input("IPv4 address: ").strip()))
    # validate(input("IPv4 address: ").strip())


def validate(ip):
    if re.search(r"^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$", ip):
        lst = ip.split(".")
        for num in lst:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
