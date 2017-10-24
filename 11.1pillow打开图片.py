from PIL import Image, ImageFilter
#pillow 文档http://pillow.readthedocs.org/
#打开图片，并新建一个名为logo_blurred.jpg的图片
kitten = Image.open("logo.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("logo_blurred.jpg")
blurryKitten.show()