def main():
    camelCase = input('camelCase: ')
    print(snake_case(camelCase))


def snake_case(camelCase):
    # TODO:
    # create an empty variable to store the new string
    # loop through the given string(camelCase) returning the index of each char and the char itself using the enumerate() function
    # if not just append the char to the empty variable created earlier
    # check if the char at the particular index is uppercase
    # if True prepend the char with '_'
    # convert the whole string to lowercase and return
    s_case = ''
    for i, char in enumerate(camelCase):
        if i and char.isupper():
            s_case += '_'

        s_case += char
    return s_case.lower()


if __name__ == '__main__':
    main()
