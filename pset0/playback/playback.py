def main():
    # prompt the user for some text input
    text = input("What would you like to say? ") or "Hello, world!"
    print(playback(text))


# create a function to replace all whitespace within the function with "..."
    # and return the result to the main function
def playback(msg):
    return msg.replace(" ", "...")


main()
