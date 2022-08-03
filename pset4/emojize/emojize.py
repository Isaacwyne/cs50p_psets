import emoji

def main():
    string = input('Input: ')
    print(emoji.emojize(f'Output: {string}', language='alias'))


if __name__ == "__main__":
    main()
