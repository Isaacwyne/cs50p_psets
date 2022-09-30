# TODO
# prompt the user for a mathematical expression
# split the expression so as to assign each one to a variable

def main():
    expression = input('Enter expression: ')
    x, y, z = expression.split(' ')
    print(round(arithmetic(x, y, z), 1))


def arithmetic(x, y, z):
    # check for the given math operator and perform the appropriate calculation
    if (y == '+'):
        return (float(x) + float(z))
    elif (y == '-'):
        return (float(x) - float(z))
    elif (y == '*'):
        return (float(x) * float(z))
    elif (y == '/'):
        return (float(x) / float(z))
    else:
        return ('Please enter a valid mathematical expression')


main()
