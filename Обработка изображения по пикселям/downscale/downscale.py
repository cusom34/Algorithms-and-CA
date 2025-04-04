import time
from PIL import Image, ImageDraw
import numpy as np

#Import image and get its dimensions

image = Image.open('kitty2.jpg')

width, height = image.size

#Create a new empty image

new_width, new_height = 480, 320
scaled_image = Image.new(image.mode, (new_width, new_height), 'white')

scale_x = new_width/width
scale_y = new_height/height

box_width = int(np.ceil(1/scale_x))
box_height = int(np.ceil(1/scale_y))
image_array = np.array(image)

tic = time.perf_counter()
for i in range(new_height):
    for j in range(new_width):
        
        #Coordinates in old image
        
        x = int(np.floor(j/scale_x))
        y = int(np.floor(i/scale_y))
        
        #min() is used to assure that coordinates aren't out of bounds
        
        x_end = min(x + box_width, width-1)
        y_end = min(y + box_height, height-1)
            
        #We average the colors in the box
        
        pixel = image_array[y:y_end, x:x_end].mean(axis=(0,1))
        
        #We convert results to a tuple of ints
        
        pixel = np.round(pixel)
        pixel = tuple(pixel.astype(int))
        scaled_image.putpixel((j, i), pixel)
        
scaled_image.save("kitty3.jpg", "JPEG")
toc = time.perf_counter()
        
print(f"Вычисление заняло {toc - tic:0.4f} секунд")


#****************************************************************************#
scaled_image = Image.new(image.mode, (new_width, new_height), 'white')
tic = time.perf_counter()
for i in range(new_height):
    for j in range(new_width):
        
        x = int(np.floor(j/scale_x))
        y = int(np.floor(i/scale_y))
        
        pixel = image_array[y,x]
        
        pixel = np.round(pixel)
        pixel = tuple(pixel.astype(int))
        scaled_image.putpixel((j, i), pixel)
        
scaled_image.save("kitty4.jpg", "JPEG")
toc = time.perf_counter()
        
print(f"Вычисление заняло {toc - tic:0.4f} секунд")       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    