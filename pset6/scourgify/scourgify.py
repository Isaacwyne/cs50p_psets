import sys
import csv


def main():
    if is_valid():
        try:
            # create empty list to store the names and houses from the file(sys.argv[1])
            students = []
            # open the first file for reading
            with open(sys.argv[1]) as csvfile:
                reader = csv.DictReader(csvfile)
                # for every row in the file append the name & house to the students' list
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})
            # open the second file for writing
            with open(sys.argv[2], "w") as file:
                # add the headers and write them to the file
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for item in students:
                    last, first = item["name"].split(", ")
                    house = item["house"]
                    # write everything to the file
                    writer.writerow({"first": first, "last": last, "house": house})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def is_valid():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (sys.argv[1] and sys.argv[2]).endswith(".csv") is True and len(sys.argv) == 3:
        return True
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
