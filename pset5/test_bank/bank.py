def main():
    # TODO
    """
    - prompt the user a greeting of their choice
    - treat the user's greeting case-insensitively by converting it to lowercase and remove all the whitespace at both the beginning and end of the string.
    """

    greeting = input('Enter greeting: ')
    print(f'${value(greeting)}')


# TODO
"""
- create a new function to do all the evaluation (greetingCheck())
- check if the string begins with the word 'hello'
- also check if the string start with the letter 'h'
- if the string doesn't any of the above conditions; return '$100'
"""


def value(greeting):
    greeting = greeting.lower().strip()
    if (greeting.startswith('hello')):
        return 0
    elif (greeting.startswith('h')):
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
