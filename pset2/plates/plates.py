def main():
    try:
        plate = input("Plate: ")
        if is_valid(plate):
            print('Valid')
        else:
            print('Invalid')
    except KeyboardInterrupt:
        return


# create a function to check for the length of the input string
def length(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False


# a function to check if the string contains punctuation mrks or spaces
def contains_mrks(s):
    if not any(i in s for i in [',', '.', '?', ' ', '!', '_', '_']):
        return True
    else:
        return False


def mid_nums(s):
    # TODO
    # check for the first occurrence of a number
    # find it's index and slice the string and create a sub_string
    # loop through the string to see if it contains any letters and if list[0] == 0
    if any(element.isdigit() for element in s):
        tmp = []
        for i in s:
            if i.isdigit():
                tmp.append(i)
        index = s.index(tmp[0])
        sub_s = s[index:]
        if not any(char.isalpha() for char in sub_s) and sub_s[0] != '0':
            return True
        else:
            return False
    else:
        return True


def is_valid(s):
    # evaluate if the string meets all the conditions
    if length(s) == True and s[0].isalpha() and s[1].isalpha() and contains_mrks(s) and mid_nums(s):
        return True
    else:
        return False


if __name__ == "__main__":
    main() 