# TODO
# prompt the user for a file name
# using the '.partition(sep), split the filename into a 3-tuple'
# remove whitespaces on both sides of the string

def main():
    fileName = input('Enter filename: ').strip().lower().partition('.')

    # extract only the file extension
    extension = fileName[-1]
    print(mediaType(extension))


def mediaType(extension):
    # create a switch case statement to match any of the extensions to their respective media types
    # and return 'application/octet-stream' for any other extensions that are not part of the program

    match extension:
        case 'gif':
            return 'image/gif'
        case 'jpg' | 'jpeg':
            return 'image/jpeg'
        case 'png':
            return 'image/png'
        case 'pdf':
            return 'application/pdf'
        case 'txt':
            return 'text/plain'
        case 'zip':
            return 'application/zip'
        case _:
            return 'application/octet-stream'


main()
