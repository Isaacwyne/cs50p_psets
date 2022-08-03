from inflect import engine


def main():
    e = engine()
    name_list = []
    while True:
        try:
            name = input('Name: ').title().strip()
            name_list.append(name)
        except EOFError:
            print()
            break
    print(f'Adieu, adieu, to {e.join(name_list)}')


if __name__ == '__main__':
    main()