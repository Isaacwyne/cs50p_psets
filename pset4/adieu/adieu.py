from inflect import engine


def main():
    e = engine()
    name_list = []
    while True:
        try:
            name = input('Name: ').title().strip()
            name_list.append(name)
        except EOFError:
            break
    print(f'Adieu, adieu {e.join(name_list)}')


if __name__ == '__main__':
    main()