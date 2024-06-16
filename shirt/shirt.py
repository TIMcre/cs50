import sys
from PIL import Image, ImageOps







def check_length():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_type(type):

    if sys.argv[1].endswith(type) or sys.argv[2].endswith(type):
        return True
    return False


def modifie_image():
    output = []
    try:
        picture = Image.open(sys.argv[1])
        overlay_shirt = Image.open("shirt.png")
        picture = ImageOps.fit(picture, overlay_shirt.size)
        picture.paste(overlay_shirt, overlay_shirt)
        picture.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")
    return output


def check():
    check_length()
    if not (check_type(".jpg") or not check_type(".jpeg") or not check_type(".png")):
        sys.exit("Not a valid image file (jpg, jpeg, or png)")

    if not sys.argv[1].split(".")[-1] == sys.argv[2].split(".")[-1]:
        sys.exit("Not same file extension on both files")


if __name__ == "__main__":
    check()
    modifie_image()

