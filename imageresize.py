
from PIL import Image
import glob
import pandas as pd


df = pd.read_csv('database.csv')
post_id = df.iloc[-1, 0]

list_of_images = glob.glob(f'assets/{post_id}/*.png')

print(list_of_images)


def change_image(image, filename):
    img = Image.open(image)
    new_size = (round(img.size[0]*1.5), round(img.size[1]*1.5))
    new_img = img.resize(new_size)
    image_blank = Image.new('RGBA', (1080, 1920))
    image_blank.paste(new_img, (200, 800), mask=new_img)

    screenshotPath = f'assets/{post_id}/{filename}.png'

    image_blank.save(screenshotPath)

    # image_blank.show()
count = 0
for i in list_of_images:

    change_image(i, count)
    count += 1
