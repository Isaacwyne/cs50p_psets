import validators


def main():
    user_email = input("What's your email address? ").strip()
    if validators.email(user_email) is True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
