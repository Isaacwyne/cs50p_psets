def main():
    # TODO
    # prompt the user for input
    # make sure to remove whitespace before and after the string
    # force the string to lower case

    answer = input('What is the Answer to the Great Question of Life, the Universe and Everything? ').lower().strip()
    print(evaluation(answer))


def evaluation(answer):
    # TODO
    # check if the "answer" variable is equivalent to any of the three possibilities
    # use the "or" operator because it will return "True" if anyone of them is equal to the "possibilities"

    if (answer == '42' or answer == 'forty-two' or answer == 'forty two'):
        return ('Yes')
    else:
        return ('No')


main()