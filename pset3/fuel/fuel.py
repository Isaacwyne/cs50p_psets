def main():
    # TODO:
    # prompt the usr for a fraction
    # split it and perform needed calculation
    # catch exceptions that would arise and continuously prompt the usr until they corporate
    print(calculate("Fraction: "))


def calculate(qn):
    while True:
        try:
            x, y = input(qn).split("/")
            percentage = round(int(x) / int(y) * 100)
            if percentage > 100:
                raise ValueError("percentage is above 100")
            elif percentage >= 99 and percentage <= 100:
                return "F"
            elif percentage <= 1:
                return "E"
            else:
                return f"{percentage}%"
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()