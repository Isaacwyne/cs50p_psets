import sys


def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        if (y == "0"):
            raise ZeroDivisionError("Can't divide by Zero")
        elif (x.isdigit() and y.isdigit()) is False:
            raise ValueError("percentage is above 100")
        elif (int(x) > int(y)):
            raise ValueError("percentage is above 100")
        else:
            return round(int(x) / int(y) * 100)
    except (EOFError, KeyboardInterrupt):
        sys.exit()


def gauge(percentage):
    if percentage >= 99 and percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
