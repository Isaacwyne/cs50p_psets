import random


def main():
    round_count = 1
    score = 0
    level = get_level()
    while round_count <= 10:
        x,y = generate_integer(level)
        answer = tries_count(x,y)
        if answer == True:
            score += 1
        round_count += 1
    print(f'Score: {score}')


# get level from user [should be 1,2 or 3]
# should raise a 'ValueError' if 'level' is not 1,2 or 3
def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    # randomly generate a non-negative integer with level number of digits
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y


def tries_count(x,y):
    # keep track of the user tries
    count = 1
    while count <= 3:
        try:
            ans = int(input(f'{x} + {y} = '))
            if ans == (x + y):
                return True
            else:
                count += 1
                print('EEE')
        except:
            count += 1
            print('EEE')
    print(f'{x} + {y} = {x+y}')
    return False


if __name__ == '__main__':
    main()
