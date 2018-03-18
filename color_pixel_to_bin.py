#! - color_pixel_to_bin.py
#! - Scans entire image and gives 0 or 1 depending on the color of the pixel

from PIL import Image

im = Image.open("C:\\path\\to\\file")
im = im.convert("RGBA")
datas = im.getdata()

for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        print("0")
    elif item[0] == 128 and item[1] == 128 and item[2] == 128:
        print("1")

