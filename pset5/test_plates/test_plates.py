from plates import is_valid


# check if string is of the right length
def test_length():
    valid = ['CS', 'CS50', 'ABCS', 'ABSD', 'CAT3']
    for s in valid:
        assert is_valid(s) == True
    assert is_valid('C') == False


# check if the string contains punctuation marks
def test_punctuation():
    strs = ['CS50!', 'CAT\'S', 'CS,DC', 'S_MAN!']
    for s in strs:
        assert is_valid(s) == False


# check if the numbers in the string start with a 'zero'
def test_numbers():
    for s in ['CS05', 'CS50P', '50CENT']:
        assert is_valid(s) == False


# check if meets all conditions
def test_is_valid():
    for s in ['CS05', 'CS50P', 'PI3.14', '22', 'H', 'OUTATIME']:
        assert is_valid(s) == False

    assert is_valid('CS50') == True
    assert is_valid('AAA222') == True
