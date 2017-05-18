from skimage import novice
from skimage import data

picture = novice.open(data.data_dir+'/chelsea.png')

for pixel in picture:
	pixel.red = 0
	pixel.blue = 0
	pixel.green = 255

picture.show()
picture.save('green_texture.jpg')

for pixel in picture:
	pixel.red = 0
	pixel.blue = 0
	pixel.green = 240
picture.save('green_texture2.jpg')

for pixel in picture:
	pixel.red = 0
	pixel.blue = 0
	pixel.green = 230
picture.save('green_texture3.jpg')


