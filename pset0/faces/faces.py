# implement a function called "main"
# prompt the user for input
def main():
    text = input("What would you like to say? ") or "Hello, world! :)"
    print(convert(text))


# implement another function "convert" that returns the result.
# replace the emoticons with emojis using the replace function.
def convert(msg):
    return msg.replace(":)", "🙂").replace(":(", "🙁")


main()
