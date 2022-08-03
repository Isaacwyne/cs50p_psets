months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def main():
    # TODO: split the user input into MM/DD/YYYY format
    # and if month is written in words then check for its index in list and add 1 to get month number
    # else just prefix it with a zero if its not two places
    # make sure days are not more than 31
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                try:
                    if withIn_range(day, month):
                        break
                except ValueError:
                    continue
            elif "," in date:
                month, day, year = date.split(" ")
                month = month.title()
                day = day.replace(",", "")
                if month in months:
                    month = months.index(month) + 1
                try:
                    if withIn_range(day, month):
                        break
                except ValueError:
                    continue
        except EOFError:
            return
    print(f"{year}-{int(month):02}-{int(day):02}")


def withIn_range(day, month):
    if (int(month) > 1 and int(month) <= 12) and (int(day) > 1 and int(day) <= 31):
        return True


if __name__ == '__main__':
    main()
