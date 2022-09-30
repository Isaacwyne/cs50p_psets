from twttr import shorten


def main():
    test_letter_cases()
    test_numbers()


def test_letter_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('David') == 'Dvd'
    assert shorten('PyTest') == 'PyTst'
    assert shorten('Apples') == 'ppls'


def test_numbers():
    assert shorten('cs50') == 'cs50'
    assert shorten('50 apples') == '50 ppls'


def test_punctuation():
    assert shorten('What\'s your name?') == 'Wht\'s yr nm?'
    assert shorten('<module>') == '<mdl>'


if __name__ == '__main__':
    main()
