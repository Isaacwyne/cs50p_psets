def main():
    # TODO
    # prompt the user for a string
    # create a string of the characters to be stripped from the input string.
    string = input("Input: ")
    vowels = "aeiouAEIOU"
    print(f'Output: {strip_chars(string, vowels)}')
    

def strip_chars(string, vowels):
    # create a list to temporarily store the return characters
    # loop through the string checking if the nth char is == to the vowels
    # and if != append the nth char to the 's' list
    # finally join the list into a string and return it
    s = []
    for c in string:
        if c not in vowels:
            s.append(c)
    return ''.join(s)


if __name__ == "__main__":
    main()
