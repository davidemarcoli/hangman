# importing image object from PIL
import os

from PIL import ImageOps, Image
import PIL.Image

# loop through the images in images/png
for i in os.listdir("images/png"):
    # if the file is not a png file, skip it
    if not i.endswith(".png"):
        continue
    # open the image
    img = Image.open("images/png/" + i).convert("L")
    # colorize the image to white
    # img = ImageOps.colorize(img, black="white", white="black")
    img = img.convert("RGBA")

    img.save("images/png/colorized/test" + i, "PNG")

    data = img.getdata()
    newData = []
    for item in data:
        print(item)
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((255-item[0], 255-item[1], 255-item[2], 255))

    img.putdata(newData)

    # create a folder for the colorized images
    if not os.path.exists("images/png/colorized"):
        os.makedirs("images/png/colorized")

    # write the image to the folder images/png/colorized with the same name
    img.save("images/png/colorized/" + i, "PNG")