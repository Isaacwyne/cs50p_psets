def main():
    # prompt the user for the time
    time = input('What time is it? ')
    hrs, mins = evaluation(time)
    print(convert(hrs, mins))
    

# adding 12-hour-format support
# check if the user input ends with an 'a.m.' or 'p.m.' suffix
def evaluation(time):
    if time.endswith('a.m.'):
        time = time.removesuffix('a.m.')
        hrs, mins = time.split(':')
        return float(hrs), float(mins)
    elif time.endswith('p.m.'):
        time = time.removesuffix('p.m.')
        hrs, mins = time.split(':')
        return float(hrs) + 12, float(mins)
    else:
        hrs, mins = time.split(':')
        return float(hrs), float(mins)


def convert(hrs, mins):
    # split the "time" variable into hrs & mins
    minsInAnHour = 60

    # convert the hrs & mins to a floating number
    # convert both the hrs & mins to floats and then multiple the hrs by the number of mins in an hour
    # to convert the hrs to mins
    # add both of them and divide them by 60 (mins in an hour) to get the final result

    convertedTime = ((hrs * minsInAnHour) + mins) / minsInAnHour

    # found the shorthand of this expression:
    # if (convertedTime >= 7) and (convertedTime <= 8):
    # on stackoverflow [https://stackoverflow.com/questions/20308588/is-there-a-greater-than-but-less-than-function-in-python]

    if (7 <= convertedTime <= 8):
        return 'breakfast time'
    elif (12 <= convertedTime <= 13):
        return 'lunch time'
    elif (18 <= convertedTime <= 19):
        return 'dinner time'
    else:
        return


if __name__ == "__main__":
    main()
