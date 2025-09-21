import imageio.v3 as iio

#Choosing which images to use

filenames = ['gif_img_1.webp', 'gif_img_2.webp','gif_img_3.webp','gif_img_4.webp','gif_img_5.webp','gif_img_6.webp']
images = [ ]

#Generating gif
for filename in filenames:
  images.append(iio.imread(filename))


iio.imwrite('Generated Gif.gif', images, duration = 500, loop = 0)




