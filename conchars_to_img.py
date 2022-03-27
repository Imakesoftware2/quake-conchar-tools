import struct
import argparse
from PIL import Image

conchars_size = (128, 128)

parser = argparse.ArgumentParser(description='Converts Quake conchars back to an image.')

parser.add_argument('--size', default=conchars_size, type=int, nargs=2)

parser.add_argument('input_img', type=str,
                    help='Input conchars.')

parser.add_argument('output_chrs', type=str,
                    help='Output image.')

args = parser.parse_args()

palette = Image.open("palette.png")

im = Image.new(mode="P", size=args.size)
im.putpalette(palette.getpalette())
palette.close()

pixels = im.load()

with open("conchars.lmp", "rb") as fp:
    for w in range(args.size[0]):
        for h in range(args.size[1]):
            color = struct.unpack("B", fp.read(1))[0]
            pixels[h,w] = color

im.save("conchars.png")
im.close()
