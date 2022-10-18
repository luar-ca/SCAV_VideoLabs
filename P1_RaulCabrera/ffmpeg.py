"""""
Exercise 2 & 3:
Use of FFMPEG to:
    - resize images.
    - convert images into black and white.
"""""
import os

# For the compression, input image of Lenna has to be JPG because otherwise, it
# will not be that noticeable in the results with an PNG.

# RESIZE
"""""
# To obtain a resized image version of the one we provide as input,
# we need to call ffmpeg and apply a filter which will scale the input Lenna into the size we indicate.
"""""
os.system("ffmpeg -i lenna.jpg -filter:v scale=1020:1020 outSIZE.jpg")


# BLACK AND WHITE
"""""
To obtain an output in black and white we can make use
of two options, when we call ffmpeg:
First one is related with the saturation, if saturation is 0, there is no pure color.
Second one is about format filter, to achieve a compressed image with grayscale filter.
"""""

# SATURATION
os.system("ffmpeg -i lenna.jpg -vf hue=s=0 outSAT.jpg")

# GRAYSCALE FILTER
os.system("ffmpeg -i lenna.jpg -vf format=gray outGRAY.jpg")


# RESULTS
"""""
When we apply the grayscale filter, compression is visible in certain zones around the image,
specially in the background. These parts of the image show a significant reduction in quality
compared to the input.

Same happens when we resize the input image into a greater size, in the first case. We see
a lower quality in comparison.

However, when we simply put the saturation to 0, there is no loss of quality.
"""""
