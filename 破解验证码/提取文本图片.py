'''提取文本图片'''
from PIL import Image

im  = Image.open('captcha.gif')
#将图片转换为8为像素模式
im.convert('P')
im2 = Image.new("P",im.size,255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227:
            im2.putpixel((y,x),0)

im2.show()
