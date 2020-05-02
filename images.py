from PIL import Image,ImageFilter
img=Image.open('./starwars.jpg')
print(img.size)
img.thumbnail((400,200))
img.save("s2.jpg",)
