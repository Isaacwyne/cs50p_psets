import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r"^(([1-9][0-2]*)\:?(([0-5][0-9])*) (?:[A|P]M)) to (([1-9][0-2]*)\:?(([0-5][0-9])*) (?:[A|P]M))$", s)
    if time:
        hr1 = int(time.group(2))
        hr2 = int(time.group(6))
        group1 = time.group(1)
        group2 = time.group(5)

        # Left-hand side
        if is_AM(group1) is True and hr1 == 12:
            hr1 -= 12
        elif is_AM(group1) is False:
            if hr1 == 12:
                hr1 == hr1
            else:
                hr1 += 12
        if 4 <= len(group1) <= 5:
            lhs_tym = f"{hr1:02}:00"
        else:
            lhs_tym = f"{hr1:02}:{time.group(3)}"

        # Right-hand side
        if is_AM(group2) is True and hr2 == 12:
            hr2 -= 12
        elif is_AM(group2) is False:
            if hr2 == 12:
                hr2 == hr2
            else:
                hr2 += 12
        if 4 <= len(group2) <= 5:
            rhs_tym = f"{hr2:02}:00"
        else:
            rhs_tym = f"{hr2:02}:{time.group(7)}"

        return f"{lhs_tym} to {rhs_tym}"
    else:
        raise ValueError


def is_AM(s):
    return True if s.endswith("AM") else False


if __name__ == "__main__":
    main()
