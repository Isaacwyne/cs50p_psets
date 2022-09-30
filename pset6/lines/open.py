# for _ in range(3):
#     name = input("What's your name? ")

#     with open("names.txt", "a") as file:
#         file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for i in file:
#         print(i.strip())

with open("names.txt", "r") as file:
    for line in file:
        name, sex = line.rstrip().split(",")
        print(f"{name} is {sex}")

# the sorted list can be reversed using reverse and setting it to True
# for name in sorted(lines):
#     print("hello,", name.rstrip())

# check the number of names in the file
# print(len(lines))
