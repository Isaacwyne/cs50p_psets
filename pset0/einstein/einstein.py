def main():
    # prompt the user for mass as an integer
    mass = int(input("Enter mass here: "))
    print(calculate(mass))


def calculate(mass):
    return mass * 300000000 ** 2


main()
