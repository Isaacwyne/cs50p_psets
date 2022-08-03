import sys
import random
from pyfiglet import Figlet

# expects 0 or 2 command-line arguments
# if arguments == 0; output txt with random font
# if arguments == 2; output txt in user specified font


def main():
    # prompt the user for text
    if len(sys.argv) == 1:
        isPrefixed = False
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv == '--font'):
        # check if the arguments are '-f' or '--font' and a name of a font is provided
        isPrefixed = True
    else:
        sys.exit('Invalid usage')

    txt = input('Input: ')
    if isPrefixed == True:
        print(f'Output: \n{prefixed(txt)}')
    else:
        print(f'Output: \n{default(txt)}')


def default(txt):
    font = Figlet(font=random.choice(Figlet().getFonts()))
    return font.renderText(txt)


def prefixed(txt):
    font = Figlet(font=sys.argv[2])
    return font.renderText(txt)


if __name__ == "__main__":
    main()