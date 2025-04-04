from PIL import Image, ImageDraw

image = Image.open("kitty.jpg")
image = image.convert("RGB")
draw = ImageDraw.Draw(image)
width, height = image.size
pix = image.load()

new_image = Image.new('RGB', (width*2-1, height*2-1), 'black')
new_draw = ImageDraw.Draw(new_image)
for i in range(0,height):
   for j in range(0,width):
        r, g, b = pix[j, i]
        if (j+1<width) : r1, g1, b1 = pix[j+1, i]
        if (i + 1 < height): r2, g2, b2 = pix[j, i+1]

        new_draw.point((2*j,2*i), (r, g, b))
        new_draw.point((2*j-1, 2*i), (int((r+r1)/2),int((g+g1)/2),int((b+b1)/2)))
        new_draw.point((2*j, 2*i-1), (int((r + r2) / 2), int((g + g2) / 2), int((b + b2) / 2)))
        new_draw.point((2 * j -1, 2 * i -1), (int((r1 + r2 + r) / 3), int((g1 + g2+ g) / 3), int((b1 + b2+ b) / 3)))


new_image.save("kitty2.jpg", "JPEG")