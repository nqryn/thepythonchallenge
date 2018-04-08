# odd even
from PIL import Image, ImageDraw

im = Image.open("cave.jpg") 
pixels = im.load()

px = 0
py = 0
img1 = Image.new("RGB", (im.size[0]/2, im.size[1]/2))
pixels1 = img1.load()

for x in range(0, im.size[0], 2):
    for y in range(0, im.size[1], 2):
        pixels1[x/2, y/2] = pixels[x, y]

img1.show()