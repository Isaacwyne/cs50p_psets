def main():
    dollars = dollars_to_float(input('How much was the meal? '))
    percent = percent_to_float(input('What percentage would you like to tip? '))
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')


def dollars_to_float(d):
    # TODO
    # remove the '$' sign from the beginning of the string
    # and return a 'float'
    return (float(d.removeprefix('$')))


def percent_to_float(p):
    # TODO
    # remove the '%' sign from the end of the string
    # then convert percent to 'int' inorder to perform arithmetic on it (create a variable to store the integer)
    num = int(p.removesuffix('%'))
    return float(num / 100)


main()
