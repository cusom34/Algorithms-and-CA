import random 
from PIL import Image, ImageDraw

def diap(a):
    if a>255: return 255
    if a<0: return 0
    return a


image = Image.open("kitty.jpg")
image = image.convert("RGB")
draw = ImageDraw.Draw(image)
width, height = image.size
pix = image.load()
for i in range(height):
   for j in range(width):
        r, g, b = pix[j, i]
        s = int((r+g+b)/3)
        draw.point((j,i), (s,s,s))

image.save("kitty2.jpg", "JPEG")


img = Image.new('RGB', (height, width), 'black')
dr = ImageDraw.Draw(img)
for i in range(height):
   for j in range(width):
        r, g, b = pix[j, i]
        s = int((r+g+b)/3)
        dr.point((i,j), (r,g,b))

img.save("kitty3.jpg", "JPEG")


image = Image.open("kitty3.jpg")
image = image.convert("RGB")
draw = ImageDraw.Draw(image)
width, height = image.size
pix = image.load()
for i in range(height):
   for j in range(width):
        r, g, b = pix[j, i]
        ran = random.randint(0,100)
        r=diap(r+ran)
        g=diap(g+ran)
        b=diap(b+ran)
        draw.point((j,i), (r, g, b))

image.save("kitty4.jpg", "JPEG")