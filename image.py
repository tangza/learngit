# pip install Pillow

from PIL import Image

im = Image.open('img.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 135))
im.save('thumbnail.png', 'PNG')
