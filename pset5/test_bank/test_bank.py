from bank import value


def main():
    test_hello()
    # test_beginning_with_h()


# check for 'hello' and punctuation mark cases
def test_hello():
    for greeting in ['hello', 'Hello', 'hello, there', 'Hello, Sir']:
        assert value(greeting) == 0


# check for greetings that start with 'h' and not hello
def test_beginning_with_h():
    greetings = ['hola', 'How are you doing?', 'Howdy']
    for greeting in greetings:
        assert value(greeting) == 20


# and for any other greeting apart from the above cases
def test_default():
    greetings = ['what\'s up?', 'Wah gwaan']
    for greeting in greetings:
        assert value(greeting) == 100


if __name__ == '__main__':
    main()
