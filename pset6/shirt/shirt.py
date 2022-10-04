import sys
from os import path
from PIL import Image, ImageOps


def main():
    # IndexError incase not enough command-line arguments are supplied
    try:
        if valid() is True:
            try:
                shirt = Image.open("shirt.png")
                size = shirt.size
                pic = Image.open(sys.argv[1])
                cropped_pic = ImageOps.fit(pic, size, method=Image.Resampling.BICUBIC,
                        bleed=0.0, centering=(0.5, 0.5))
                cropped_pic.paste(shirt, box=None, mask=shirt)
                cropped_pic.save(sys.argv[2])
    # Exception for when the input_file doesn't exist
            except FileNotFoundError:
                sys.exit("Input does not exist")
    except IndexError:
        sys.exit("Too few command-line arguments")


def valid():
    # exactly two command-line arguments
    input_ext = path.splitext(sys.argv[1].lower())
    output_ext = path.splitext(sys.argv[2].lower())
    if not input_ext[1] in [".jpg", "jpeg", ".png"]:
        sys.exit("Invalid input")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # check if arguments have different extensions
    # check if extension is in ['.jpg', 'jpeg', 'png']
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and input_ext[1] == output_ext[1]:
        return True
    else:
        sys.exit("Not an image file")


if __name__ == "__main__":
    main()
