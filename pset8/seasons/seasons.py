from datetime import date
import sys
import re
import inflect

p = inflect.engine()


# use regex to validate user input (YYYY-MM-DD)
def main():
    birth_day = input("Date of Birth: ")
    try:
        year, month, day = validate_date(birth_day)
        date_of_birth = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    num_of_days = date.today() - date_of_birth
    total_minutes = num_of_days.days * 24 * 60
    print(f'{p.number_to_words(total_minutes, andword="").capitalize()} minutes')


def validate_date(birth_day):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_day):
        year, month, day = birth_day.split("-")
        return year, month, day
    raise ValueError


if __name__ == "__main__":
    main()
