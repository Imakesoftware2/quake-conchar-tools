import struct
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Converts an image back to Quake conchars.')

parser.add_argument('input_img', type=str,
                    help='Input image.')

parser.add_argument('output_chrs', type=str,
                    help='Output conchars.')

args = parser.parse_args()

im = Image.open(args.input_img)
pixels = im.load()

with open(args.output_chrs, "wb") as fp:
    for w in range(im.size[0]):
        for h in range(im.size[1]):
            color = struct.pack("B", pixels[h,w])
            fp.write(color)
