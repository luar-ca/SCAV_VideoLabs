import os

"""""
Exercise 3: Resize BBB video into 4 output videos with dimensions...
    720p
    480p
    360x240
    160x120
"""""

#   With 720p
os.system('ffmpeg -i big_buck_bunny.mp4 -vf scale=-1:720 bbb_720.mp4')

#   With 480p
os.system('ffmpeg -i big_buck_bunny.mp4 -vf scale=480:-1 bbb_480.mp4')


# Rescale video for fixed width/height:

# With 360x240
os.system('ffmpeg -i big_buck_bunny.mp4 -vf scale=360:240,setsar=1:1 bbb_360x240.mp4')

# With 160x120
os.system('ffmpeg -i big_buck_bunny.mp4 -vf scale=160:120,setsar=1:1 bbb_160x120.mp4')

"""""
RESULTS:
In the first two cases, as we only specify one dimension, we need to set
the other component to -1. By doing this, we keep the aspect ratio of the video in output.
The -1 component indicates that width/height of output has to be calculated according to
aspect ratio of input video.  

The next two cases have fixed dimensions to be resized. However, ffmpeg will take only
one of the two components and will set the other one in order to compensate the aspect 
ratio. To avoid that and obtain output with expected dimensions, we use setsar=1:1
(Sample Aspect Ratio).
"""""
