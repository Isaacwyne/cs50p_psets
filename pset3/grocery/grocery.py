# TODO: get user input and append it to a dictionary
# loop thru the dictionary
# and if the key already exists, increment value by one else just append with value 1
def main():
    grocery = {}
    while True:
        try:
            item = input().upper().strip()
            # check if item already exists in the dictionary
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except(EOFError):
            print()
            for key in sorted(grocery.keys()):
                print(grocery[key], key)
            break


if __name__ == "__main__":
    main()
