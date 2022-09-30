import sys
import random


def main():
    # user input
    # check if level is a positive integer
    # handle keyboard interrupt errors
    while True:
        try:
            level = int(input('Level: '))
            if level > 0:
                break
        except (EOFError, KeyboardInterrupt):
            sys.exit()
        except:
            pass

    # generate the random integer
    random_num = random.randint(1, level)

    # get 'guess' from user
    # check if the 'guess' is right
    # and reprompt the user if it ain't 
    while True:
        try:
            guess = int(input('Guess: '))
            if guess > 0:
                if guess < random_num:
                    print('Too small!')
                elif guess > random_num:
                    print('Too large!')
                else:
                    print('Just right!')
                    break
        except (EOFError, KeyboardInterrupt):
            sys.exit()
        except:
            pass


if __name__ == '__main__':
    main()