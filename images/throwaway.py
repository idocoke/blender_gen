from skimage import io

image = io.imread('000001.jpg')

h = len(image)
w = len(image[0])


for i in range(240,371):
	image[i][48] = [255,255,255]
	image[i][195] = [255,255,255]
for j in range(48,195):
	image[240][j] = [255,255,255]
	image[371][j] = [255,255,255]

io.imsave('test2.png',image)
