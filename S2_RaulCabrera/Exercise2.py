import os

"""""
Exercise 2: Extract YUV histogram of BBB video and overlay
"""""

# With the following command, YUV is extracted, scaled and overlaid over BBB video
command = 'ffmpeg -y -i big_buck_bunny.mp4 -vf ' \
          '"split=2[a][b],[b]histogram,format=yuva444p,scale=100:100[hh],[a][hh]overlay" ' \
          'video_histogram.mp4'

os.system(command)
