# analisando e manipulando imagens com pillow
from PIL import Image
from PIL import ImageEnhance


img = Image.open('data/photo.jpg')
img.show()

gray_img = img.convert('L') # torna a cor da imagem cinza

rotate_img = img.rotate(45)

transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)

resize_image_small = img.resize((300, 200))

resize_image_big = img.resize((1500, 800))

dimension = (1500, 4000, 3500, 5300)
crop_img = img.crop(dimension)

bright = ImageEnhance.Brightness(img)
bright_img = bright.enhance(2)

contrast = ImageEnhance.Contrast(img)
contrast_img = contrast.enhance(2)

gray_img.save("output/gray.jpg")
rotate_img.save("output/rotate.jpg")
transpose_img.save("output/flip.jpg")
resize_image_small.save("output/small.jpg")
resize_image_big.save("output/big.jpg")
crop_img.save("output/crop.jpg")
bright_img.save("output/bright.jpg")
contrast_img.save("output/contrast.jpg")


